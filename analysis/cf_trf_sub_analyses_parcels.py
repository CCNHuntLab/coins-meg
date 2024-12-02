"""
Perform subject-level analyses of TRF estimates on source-reconstructed parcellated data.
"""

import argparse
import cf_parcellation
import cf_trf
import cf_trf_analyses
import cf_utils
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
    effects = ["laserMiss-minus-laserHit", "laserMiss-plus-laserHit"]

    # Types of values to compute from the original signal
    signaltypes = ["signal", "z-signal"]
    
    # Baseline period to compute relative signal value
    baseline_window = (-0.2, 0.)

    # Output directory in which the TRFs have been saved and in which the
    # results of this script will be saved
    outdir_parent = "./gitignore/results"

    # Selection of parcels for which to analyze the TRFs, specified by names.
    parcel_names = cf_parcellation.get_parcel_names_2hemi([
                     "Primary and Early Visual Cortex",
                     "Anterior Cingulate and Medial Prefrontal Cortex",
                     "Early Auditory Cortex",
                     ])

    # Subjects to analyze
    subs = [4] # coinsmeg.SUB_NUMS_ALL

    ########################################################
    # Analysis code
    ########################################################

    cf_utils.create_dir_if_needed(outdir_parent)
    cf_utils.setup_mpl_style()

    event_names = ["laserHit", "laserMiss"]
    events = '-'.join([str(coinsmeg.EVENT_ID[ev]) for ev in event_names])
    datatype = "parcels"

    for sub in subs:
        print(f"Running subject {sub}")
        # Load the TRFs
        outdir = op.join(outdir_parent, coinsmeg.sub_num2str(sub))
        trfs_fpath = cf_trf.get_trfs_fpath(outdir, sub, events, datatype)
        trfs = cf_trf.load_trfs(trfs_fpath)
        if trfs is None:
            print(f"Skipping subject {sub} because we don't have TRFs for {datatype}")
            continue
        #
        # Compute and plot the evoked responses for each considered effect
        # and signal type.
        #
        for effect, signaltype in itertools.product(effects, signaltypes):
            # Compute the evoked response
            evoked_by_ev = {ev: trfs[event_names.index(ev)].copy() for ev in event_names}
            evoked = cf_trf_analyses.compute_evoked_response(evoked_by_ev,
                effect, signaltype, baseline_window=baseline_window)
            has_baseline = "rel" in signaltype or "z" in signaltype
            has_zscore = ("z" in signaltype)
            units = "Z-Beta coef." if has_zscore else "Beta coef."
            scalings = 1
            highlight = (baseline_window if has_baseline else None)
            #
            # Plot the evoked response time course for all selected parcels
            #
            # Plot each parcel on a separate figure
            for parcel_name in parcel_names:
                parcel_idx = cf_parcellation.get_parcel_idx_with_name(parcel_name)
                pretty_name = cf_parcellation.get_pretty_name(parcel_name)
                # Plot parcel time course and location separately
                title = f"TRF for {effect}, {parcel_name} (subject {sub}, {signaltype})"
                fig = cf_trf_analyses.plot_parcels_timecourse(evoked,
                    [parcel_idx], [parcel_name], do_legend=False, do_color=False,
                    ylabel=units, highlight=highlight, title=title)
                figname = "trf-parcel-timecourse"
                paramkeys = ["effect", "datatype", "signaltype", "parcel"]
                paramvals = [effect, datatype, signaltype, parcel_idx]
                fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
                fpath = cf_utils.path_with_components(outdir, fname, "png")
                cf_utils.save_figure(fig, fpath)
                fig = cf_trf_analyses.plot_parcel_location(parcel_idx, parcel_name,
                    title=pretty_name)
                figname = "trf-parcel-loc"
                paramkeys = ["parcel"]
                paramvals = [parcel_idx]
                fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
                fpath = cf_utils.path_with_components(outdir, fname, "png")
                cf_utils.save_figure(fig, fpath)
                # Plot parcel time course and location on the same figure
                fig, axes = plt.subplots(nrows=2, figsize=(6.4, 6),
                    height_ratios=[1, 1])
                ax = axes[0]
                title = f"TRF for {effect} (subject {sub}, {signaltype})"
                fig = cf_trf_analyses.plot_parcels_timecourse(evoked,
                    [parcel_idx], [parcel_name], ax=ax,
                    do_legend=False, do_color=False,
                    ylabel=units, highlight=highlight, title=title)
                ax = axes[1]
                cf_trf_analyses.plot_parcel_location(parcel_idx, parcel_name, ax=ax,
                    title=pretty_name)
                figname = "trf-parcel-timecourse-and-loc"
                paramkeys = ["effect", "datatype", "signaltype", "parcel"]
                paramvals = [effect, datatype, signaltype, parcel_idx]
                fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
                fpath = cf_utils.path_with_components(outdir, fname, "png")
                cf_utils.save_figure(fig, fpath)
            # Plot all parcels together on the same figure
            parcel_indices = cf_parcellation.get_parcel_idx_with_names(parcel_names)
            title = f"TRF for {effect} (subject {sub}, {signaltype})"
            fig = cf_trf_analyses.plot_parcels_timecourse(evoked,
                parcel_indices, parcel_names,
                ylabel=units, highlight=highlight, title=title)
            figname = "trf-parcels-timecourse"
            paramkeys = ["effect", "datatype", "signaltype", "parcels"]
            paramvals = [effect, datatype, signaltype, "-".join([str(idx) for idx in parcel_indices])]
            fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
            fpath = cf_utils.path_with_components(outdir, fname, "png")
            cf_utils.save_figure(fig, fpath)

if __name__ == '__main__':
    main()