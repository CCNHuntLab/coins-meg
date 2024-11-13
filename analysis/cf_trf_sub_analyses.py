"""
Perform subject-level analyses of TRF estimates.
"""

import argparse
import cf_utils
import cf_trf
import cf_trf_analyses
import coinsmeg_data as coinsmeg
import itertools
import numpy as np
import matplotlib.pyplot as plt
import mne
import os.path as op

def main():
    ########################################################
    # Parameters for the analysis
    ########################################################

    # Effects of interest, for which to analyze the MEG responses.
    # - laserHit, laserMiss: Response to single events
    # - laserMiss-minus-laserHit: Comparison between the responses to laserMiss
    #   vs. laserHit
    # - laserMiss-plus-laserHit: Sum of the two responses, corresponding to the
    #   response to the occurrence of a laser (irrespective of whether it was
    #   hit or miss)
    effects = ["laserHit", "laserMiss", "laserMiss-minus-laserHit", "laserMiss-plus-laserHit"]

    # Types of values to compute from the original signal that determines which values are used for the analysis of the MEG
    # signal.
    # - rel-signal: The signal value relative to baseline (signal - baseline).
    #   The baseline is computed by averaging the signal over the specified
    #   baseline period.
    # - z-signal: The z-scored signal value. The mean and std used for the
    #   z-scoring are the mean and std of the signal in the baseline period.
    signaltypes = ["signal", "rel-signal", "z-signal"]
    
    # Baseline period to compute relative signal value
    baseline_window = (-0.2, 0.)

    # Output directory in which the TRFs have been saved and in which the
    # results of this script will be saved
    outdir_parent = "./gitignore/results"

    # Type of MEG sensor data to analyze. At the moment we only use mag data,
    # because plotting negative values obtained from grad data (which occur
    # when computing differences) does not work well with MNE.
    datatypes = ["mag"]

    ########################################################
    # Analysis code
    ########################################################

    cf_utils.create_dir_if_needed(outdir_parent)
    cf_utils.setup_mpl_style()

    for sub in coinsmeg.SUB_NUMS_ALL:
        print(f"Running subject {sub}")
        outdir = op.join(outdir_parent, coinsmeg.sub_num2str(sub))
        cf_utils.create_dir_if_needed(outdir)
        # Load the TRFs
        trfsd = {}
        event_names = ["laserHit", "laserMiss"]
        events = '-'.join([str(coinsmeg.EVENT_ID[ev]) for ev in event_names])
        for datatype in datatypes:
            trfs_fname = cf_trf.get_trfs_fname(sub, events, datatype)
            trfs_fpath = cf_utils.path_with_components(outdir, trfs_fname, "fif")
            if not op.exists(trfs_fpath):
                print(f"Skipping subject {sub} because we don't have TRFs for {datatype}")
                break
            trfs = cf_trf.load_trfs(trfs_fpath)
            trfsd[datatype] = trfs
        if len(trfsd) < len(datatypes):
            continue
        #
        # Compute and plot the evoked responses for each considered effect
        # and signal type.
        #
        for effect, signaltype, datatype in itertools.product(
            effects, signaltypes, datatypes):
            # Compute the evoked response
            trfs = trfsd[datatype]
            evoked_by_ev = {ev: trfs[event_names.index(ev)].copy() for ev in event_names}
            evoked = cf_trf_analyses.compute_evoked_response(evoked_by_ev,
                effect, signaltype, baseline_window=baseline_window)
            #
            # Plot the evoked response using different kinds of visualization
            # (topography, timecourse, combination of both)
            #
            has_baseline = "rel" in signaltype or "z" in signaltype
            has_zscore = ("z" in signaltype)
            title = f"TRF for {effect} (subject {sub}, {datatype}, {signaltype})"
            units = "zscore" if has_zscore else None
            scalings = 1 if has_zscore else None
            highlight = (baseline_window if has_baseline else None)
            paramkeys = ["effect", "datatype", "signaltype"]
            paramvals = [effect, datatype, signaltype]
            # Figure showing the topography at specific, manually-selected
            # time points (sampled on a grid from -100ms to 600ms).
            figname = "trf-topo"
            topomap_times = np.array([-0.1, -0.05, 0., 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35,
                0.4, 0.45, 0.5, 0.55, 0.6])
            fig = evoked.plot_topomap(times=topomap_times,
                units=units,
                scalings=scalings,
                nrows="auto", ncols=5,
                show=False)
            fig.suptitle(title)
            fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
            fpath = cf_utils.path_with_components(outdir, fname, "png")
            cf_utils.save_figure(fig, fpath)
            # Figure showing the time courses for all time points
            figname = "trf-timecourse"
            fig = mne.viz.plot_evoked(evoked,
                units=units,
                scalings=scalings,
                titles={"mag": title, "grad": title},
                spatial_colors=True,
                highlight=highlight,
                show=False)
            # fig.suptitle(title)
            fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
            fpath = cf_utils.path_with_components(outdir, fname, "png")
            cf_utils.save_figure(fig, fpath)
            # Figure showing the time courses and the topographies at
            # automatically-chosen peak times
            figname = "trf-joint"
            fig = mne.viz.plot_evoked_joint(evoked,
                times='peaks', title=title, show=False,
                exclude="bads",
                ts_args=dict(units=units, scalings=scalings, highlight=highlight),
                topomap_args=dict(units=units, scalings=scalings))
            fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
            fpath = cf_utils.path_with_components(outdir, fname, "png")
            cf_utils.save_figure(fig, fpath)

if __name__ == '__main__':
    main()