"""
Perform group-level analyses of TRF estimates on source-reconstructed parcellated data.
"""

import argparse
import cf_parcellation
import cf_utils
import cf_trf
import cf_trf_analyses
import coinsmeg_data as coinsmeg
import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import mne
import os.path as op
import scipy.sparse
import scipy.stats

def main():
    ########################################################
    # Parameters for the analysis
    ########################################################

    # Effects of interest, for which to analyze the MEG responses.
    effects = ["laserMiss-minus-laserHit", "laserMiss-plus-laserHit"]

    # Effects for which to extract and plot statistically significant clusters
    effects_to_show_sig = ["laserMiss-minus-laserHit", "laserMiss-plus-laserHit"]

    # Type that determines which values are used for the analysis of the MEG
    # signal.
    signaltypes = ["rel-signal", "z-signal", "signal"]
    
    # Baseline period to compute relative/z-scored signal value
    baseline_window = (-0.2, 0.)

    # Cluster-forming threshold for the nonparametric cluster-based statistical testing
    cluster_forming_threshold_p = 0.001

    # Clusters whose p-value is below the p_sig_cluster threshold will be considered
    # statistically significant
    p_sig_cluster = 0.05

    # Directory in which the TRFs have been saved
    indir_parent = "./gitignore/results"

    # Output directory in which the results of this script will be saved
    outdir = "./gitignore/results/group"

    # Selection of parcels for which to analyze the TRFs, specified by names.
    parcel_names = [
                     "Primary and Early Visual Cortex_rh",
                     "Anterior Cingulate and Medial Prefrontal Cortex_rh",
                     "Early Auditory Cortex_rh",
                     ]

    ########################################################
    # Analysis code
    ########################################################

    cf_utils.create_dir_if_needed(outdir)
    cf_utils.setup_mpl_style()

    event_names = ["laserHit", "laserMiss"]
    events = '-'.join([str(coinsmeg.EVENT_ID[ev]) for ev in event_names])
    datatype = "parcels"

    #
    # Compute the subject-level evoked responses for the considered effect
    # and signal type, and store the results in a dictionary.
    #
    evokedsd_subs = {}
    for sub in coinsmeg.SUB_NUMS_ALL:
        # Load the TRFs for this subject
        indir = op.join(indir_parent, coinsmeg.sub_num2str(sub))
        trfs_fpath = cf_trf.get_trfs_fpath(indir, sub, events, datatype)
        trfs = cf_trf.load_trfs(trfs_fpath)
        if trfs is None:
            print(f"Skipping subject {sub} because we don't have TRFs for {datatype}")
            continue
        evoked_by_ev = {ev: trfs[event_names.index(ev)].copy() for ev in event_names}
        # Compute the evoked response from the TRFs for each effect and signal type
        evokedsd_subs[sub] = {effect: {signaltype: None
            for signaltype in signaltypes} for effect in effects}
        for effect, signaltype in itertools.product(
            effects, signaltypes):
            evokedsd_subs[sub][effect][signaltype] = cf_trf_analyses.compute_evoked_response(
                evoked_by_ev, effect, signaltype, baseline_window=baseline_window)

    # This is the effective list of subjects that are included in the analysis
    subjects = list(evokedsd_subs.keys())

    #
    # Compute and plot the group-level evoked response for the considered
    # effect and signal type. This is done by performing a computing t-value
    # statistics across subjects. The obtained t-values constitute the
    # group-level evoked response. The t-values are then used to test for
    # statistical significance.
    #
    # A nonparametric cluster-based method is used to test for statistical
    # significance. The statistically significant clusters are then
    # extracted and plotted one at time.
    #
    for effect, signaltype in itertools.product(effects, signaltypes):
        # The measurement information used to construct the evoked response
        # is taken from an arbitrary subject, as these should be the same
        # across subjects
        sample_evoked = evokedsd_subs[subjects[0]][effect][signaltype]
        sample_info = sample_evoked.info
        info = sample_info.copy()
        # Construct the data array X for the statistical test.
        # X is an array of shape (n_subjects, n_times, n_channels).
        X = np.stack([evokedsd_subs[sub][effect][signaltype].data.T
            for sub in subjects], axis=0)
        # Adjacency matrix for the clustering of parcels: Assume no adjacency
        # between parcels. Each parcel is treated as independent and
        # unconnected.
        adjacency = scipy.sparse.eye(X.shape[-1])
        # Cluster-forming threshold, in terms of t value. T values will be
        # thresholded at this value to form clusters
        threshold_t = -scipy.stats.t.ppf(cluster_forming_threshold_p / 2, len(subjects)-1)
        # Perform the cluster-based statistical testing. The outputs of this
        # procedure are:
        # - t_vals: The t-values computed across subjects at each time point
        #   and sensor location (shape n_times, n_channels)
        # - clusters: The list of clusters that were obtained after
        #   thresholding.
        # - cluster_pv: The p-value for each cluster, determined by a
        #   nonparametric permutation test.
        t_vals, clusters, cluster_pv, H0 = mne.stats.spatio_temporal_cluster_1samp_test(
            X, adjacency=adjacency, threshold=threshold_t)
        # Construct the group-level evoked response. The data of the evoked
        # response are the t-values.
        evoked = mne.EvokedArray(t_vals.T, info,
            tmin=sample_evoked.tmin, comment=sample_evoked.comment)

        #
        # Plot the group-level evoked response time courses for all selected parcels
        #
        units = "t value"
        scalings = 1
        vlim = cf_utils.get_symmetric_vlim_for_data(evoked.data)
        ypad = (vlim[1] - vlim[0]) * 0.025
        ylim = (vlim[0]-ypad), (vlim[1]+ypad)
        has_baseline = "rel" in signaltype or "z" in signaltype
        highlight = baseline_window if has_baseline else None
        # Plot each parcel on a separate figure
        for parcel_name in parcel_names:
            parcel_idx = cf_parcellation.get_parcel_idx_with_name(parcel_name)
            pretty_name = cf_parcellation.get_pretty_name(parcel_name)
            title = f"Group-level TRF for {effect} in {pretty_name} (N={len(subjects)}, {datatype}, {signaltype})"
            fig = cf_trf_analyses.plot_parcels_timecourse(evoked,
                    [parcel_idx], [parcel_name], do_legend=False, do_color=False,
                    ylabel=units, highlight=highlight, title=title)
            paramkeys = ["effect", "datatype", "signaltype", "parcel"]
            paramvals = [effect, datatype, signaltype, parcel_idx]
            figname = "trf-parcel-timecourse"
            fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
            fpath = cf_utils.path_with_components(outdir, fname, "png")
            cf_utils.save_figure(fig, fpath)
        # Plot all parcels together on the same figure
        parcel_indices = cf_parcellation.get_parcel_idx_with_names(parcel_names)
        pretty_names = [cf_parcellation.get_pretty_name(parcel_name) for parcel_name in parcel_names]
        colors = [mpl.colormaps.get_cmap("Set1")(i) for i in range(len(parcel_indices))]
        title = f"Group-level TRF for {effect} (N={len(subjects)}, {datatype}, {signaltype})"
        fig = cf_trf_analyses.plot_parcels_timecourse(evoked,
                parcel_indices, pretty_names,
                ylabel=units, highlight=highlight, title=title, colors=colors)
        figname = "trf-parcels-timecourse"
        paramkeys = ["effect", "datatype", "signaltype", "parcels"]
        paramvals = [effect, datatype, signaltype, "-".join([str(idx) for idx in parcel_indices])]
        fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
        fpath = cf_utils.path_with_components(outdir, fname, "png")
        cf_utils.save_figure(fig, fpath)

        do_sig = (effect in effects_to_show_sig)
        if not do_sig:
            continue

        #
        # Plot the statistically significant clusters of the group-level
        # evoked response.
        #
        # TBD: Plotting to be implemented, just print the significant clusters for now
        sig_clust_inds = np.where(cluster_pv < p_sig_cluster)[0]
        print(f"sig_clust_inds for {effect} ({signaltype}): {sig_clust_inds}")

if __name__ == '__main__':
    main()
