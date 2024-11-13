"""
Perform group-level analyses of TRF estimates.
"""

import argparse
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
    # - laserHit, laserMiss: Response to single events
    # - laserMiss-minus-laserHit: Comparison between the responses to laserMiss
    #   vs. laserHit
    # - laserMiss-plus-laserHit: Sum of the two responses, corresponding to the
    #   response to the occurrence of a laser (irrespective of whether it was
    #   hit or miss)
    effects = ["laserHit", "laserMiss", "laserMiss-minus-laserHit", "laserMiss-plus-laserHit"]

    # Effects for which to extract and plot statistically significant clusters
    effects_to_show_sig = ["laserMiss-minus-laserHit", "laserMiss-plus-laserHit"]

    # Type that determines which values are used for the analysis of the MEG
    # signal.
    # - rel-signal: The signal value relative to baseline (signal - baseline).
    #   The baseline is computed by averaging the signal over the specified
    #   baseline period.
    # - z-signal: The z-scored signal value. The mean and std used for the
    #   z-scoring are the mean and std of the signal in the baseline period.
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

    # Type of MEG sensor data to analyze. At the moment we only use mag data,
    # because plotting negative values obtained from grad data (which occur
    # when computing differences) does not work well with MNE.
    datatypes = ["mag"]

    ########################################################
    # Analysis code
    ########################################################

    cf_utils.create_dir_if_needed(outdir)
    cf_utils.setup_mpl_style()

    event_names = ["laserHit", "laserMiss"]
    events = '-'.join([str(coinsmeg.EVENT_ID[ev]) for ev in event_names])
    
    for datatype in datatypes:
        #
        # Compute the subject-level evoked responses for the considered effect
        # and signal type, and store the results in a dictionary.
        #
        evokedsd_subs = {}
        for sub in coinsmeg.SUB_NUMS_ALL:
            # Load the TRFs for this subject
            indir = op.join(indir_parent, coinsmeg.sub_num2str(sub))
            trfs_fname = cf_trf.get_trfs_fname(sub, events, datatype)
            trfs_fpath = cf_utils.path_with_components(indir, trfs_fname, "fif")
            if not op.exists(trfs_fpath):
                print(f"Skipping subject {sub} because we don't have TRFs for {datatype}")
                continue
            trfs = cf_trf.load_trfs(trfs_fpath)
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
            # Find the adjacency matrix between channels. This is used to compute
            # clusters for the cluster-based statistical testing.
            ch_adjacency, ch_names = mne.channels.find_ch_adjacency(sample_info, ch_type=None)
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
                X, adjacency=ch_adjacency, threshold=threshold_t)
            # Construct the group-level evoked response. The data of the evoked
            # response are the t-values.
            evoked = mne.EvokedArray(t_vals.T, info,
                tmin=sample_evoked.tmin, comment=sample_evoked.comment)

            #
            # Plot the group-level evoked response time course and topography
            # for all channels.
            #
            suptitle = f"Group-level TRF for {effect} (N={len(subjects)}, {datatype}, {signaltype})"
            units = "t value"
            scalings = 1
            cmap = "RdBu_r"
            vlim = cf_utils.get_symmetric_vlim_for_data(evoked.data)
            cnorm = mpl.colors.Normalize(vmin=vlim[0], vmax=vlim[1],
                clip=False)
            ypad = (vlim[1] - vlim[0]) * 0.025
            ylim = (vlim[0]-ypad), (vlim[1]+ypad)
            paramkeys = ["effect", "datatype", "signaltype"]
            paramvals = [effect, datatype, signaltype]
            # Figure showing the time courses and the topographies at
            # automatically-chosen peak times
            figname = "trf-joint"
            highlight = baseline_window
            fig = mne.viz.plot_evoked_joint(evoked,
                times='peaks', title=suptitle, show=False,
                exclude="bads",
                ts_args=dict(
                    units=units,
                    scalings=scalings,
                    highlight=highlight,
                    ylim={"mag": ylim, "grad": ylim}
                    ),
                topomap_args=dict(units=units,
                    scalings=scalings,
                    cnorm=cnorm,
                    cmap=cmap,
                    ))
            fname = cf_utils.name_with_params(figname, paramkeys, paramvals)
            fpath = cf_utils.path_with_components(outdir, fname, "png")
            cf_utils.save_figure(fig, fpath)
            # Figure showing the topography at specific, manually-selected
            # time points (sampled on a grid from -100ms to 600ms).
            figname = "trf-topo"
            topomap_times = np.array([-0.1, -0.05, 0., 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35,
                0.4, 0.45, 0.5, 0.55, 0.6])
            fig = mne.viz.plot_evoked_topomap(evoked, times=topomap_times,
                units=units,
                scalings=scalings,
                cnorm=cnorm,
                cmap=cmap,
                nrows="auto", ncols=5,
                show=False)
            fig.suptitle(suptitle)
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
            # Each cluster is plotted in one figure showing, on
            # the left side, the topography of the response averaged across
            # time, and on the right, the time courses of the channels that are
            # part of the cluster.
            #
            # The below plotting code was adapted from:
            # https://mne.tools/stable/auto_tutorials/stats-sensor-space/75_cluster_ftest_spatiotemporal.html
            #
            # Loop over the clusters considered statistically significant
            sig_clust_inds = np.where(cluster_pv < p_sig_cluster)[0]
            for i_clu, clu_idx in enumerate(sig_clust_inds):
                # Unpack cluster information (channel and time points)
                time_inds, ch_inds = np.squeeze(clusters[clu_idx])
                ch_inds = np.unique(ch_inds)
                time_inds = np.unique(time_inds)
                sig_times = evoked.times[time_inds]
                # Compute average t value of the cluster across time
                # and construct a corresponding evoked response object
                # to show its topography
                t_mean = t_vals[time_inds, ...].mean(axis=0)
                evoked_mean = mne.EvokedArray(t_mean[:, np.newaxis], evoked.info, tmin=0)
                # Create mask to show which channels are significant
                mask = np.zeros((t_mean.shape[0], 1), dtype=bool)
                mask[ch_inds, :] = True
                # Initialize figure and setup axes for the topography
                # and time courses
                fig, ax_topo = plt.subplots(1, 1, figsize=(10, 3),
                    layout="constrained")
                fig.suptitle(suptitle)
                divider = make_axes_locatable(ax_topo)
                ax_colorbar = divider.append_axes("right", size="5%", pad=0.05)
                ax_signals = divider.append_axes("right", size="300%", pad=1.2)
                # Plot topography
                plot_cluster_topomap(ax_topo, ax_colorbar, evoked_mean,
                    sig_times, mask, units=units, scalings=scalings, cnorm=cnorm,
                    cmap=cmap)
                # Plot time courses
                title = f"Cluster #{i_clu + 1}"
                plot_time_courses(ax_signals, evoked, clusters, [clu_idx], cluster_pv,
                    picks=ch_inds, units=units,
                    scalings=scalings, ylim=ylim, highlight_times=sig_times,
                    title=title)
                # Save the figure
                figname = "trf-cluster"
                fname = cf_utils.name_with_params(figname, paramkeys + ["clust"], paramvals + [i_clu+1])
                fpath = cf_utils.path_with_components(outdir, fname, "png")
                cf_utils.save_figure(fig, fpath)

            #
            # Plot together significant clusters that temporally overlap in one figure,
            # as a group of clusters.
            #
            # Find groups of clusters that are overlapping in time finding the
            # connected components of a graph whose nodes are the clusters and
            # edges are drawn between clusters that overlap
            sig_clust_time_inds = [np.unique(np.squeeze(clusters[clu_idx])[0])
                for clu_idx in sig_clust_inds]
            n_sig_clusters = len(sig_clust_inds)
            overlap_matrix = np.zeros((n_sig_clusters, n_sig_clusters))
            for i_clust_1, i_clust_2 in itertools.combinations(range(n_sig_clusters), 2):
                overlap = np.intersect1d(
                    sig_clust_time_inds[i_clust_1], sig_clust_time_inds[i_clust_2])
                overlap_matrix[i_clust_1, i_clust_2] = overlap.size > 0
                overlap_matrix[i_clust_2, i_clust_1] = overlap_matrix[i_clust_1, i_clust_2]
            n_groups, sig_clust_groups = scipy.sparse.csgraph.connected_components(overlap_matrix,
                directed=False, )
            # Plot each cluster group
            for i_group in range(n_groups):
                group_clust_inds = np.where(sig_clust_groups == i_group)[0]
                if group_clust_inds.size < 2:
                    # Skip this group if there's only one cluster in it, as the 
                    # individual clusters have already been plotted above
                    continue
                # Find the time range and the channels of the group, which is
                # the union of the time ranges and channels of the clusters in
                # the group
                time_inds = np.array([], dtype=int)
                ch_inds = np.array([], dtype=int)
                for clu_idx in sig_clust_inds[group_clust_inds]:
                    clu_time_inds, clu_ch_inds = np.squeeze(clusters[clu_idx])
                    clu_ch_inds = np.unique(clu_ch_inds)
                    clu_time_inds = np.unique(clu_time_inds)
                    time_inds = np.union1d(time_inds, clu_time_inds)
                    ch_inds = np.union1d(ch_inds, clu_ch_inds)
                group_times = evoked.times[time_inds]
                # Compute average t value of the cluster group across time
                # and construct a corresponding evoked response object
                # to show its topography
                t_mean = t_vals[time_inds, ...].mean(axis=0)
                evoked_mean = mne.EvokedArray(t_mean[:, np.newaxis], evoked.info, tmin=0)
                # Create mask to show which channels are in the cluster group
                mask = np.zeros((t_mean.shape[0], 1), dtype=bool)
                mask[ch_inds, :] = True
                # Initialize figure and setup axes for the topography
                # and time courses
                fig, ax_topo = plt.subplots(1, 1, figsize=(10, 3),
                    layout="constrained")
                fig.suptitle(suptitle)
                divider = make_axes_locatable(ax_topo)
                ax_colorbar = divider.append_axes("right", size="5%", pad=0.05)
                ax_signals = divider.append_axes("right", size="300%", pad=1.2)
                # plot topography
                plot_cluster_topomap(ax_topo, ax_colorbar, evoked_mean,
                    group_times, mask, units=units, scalings=scalings, cnorm=cnorm,
                    cmap=cmap)
                # Plot time courses
                title = f"Group of clusters " + "-".join([f"{i_clu + 1}"
                    for i_clu in group_clust_inds])
                plot_time_courses(ax_signals, evoked, clusters,
                    sig_clust_inds[group_clust_inds], cluster_pv,
                    picks=ch_inds, units=units,
                    scalings=scalings, ylim=ylim, highlight_times=group_times,
                    title=title)
                # Save the figure
                figname = "trf-cluster"
                fname = cf_utils.name_with_params(figname, paramkeys + ["clust-group"], paramvals + [i_group+1])
                fpath = cf_utils.path_with_components(outdir, fname, "png")
                cf_utils.save_figure(fig, fpath)

def plot_cluster_topomap(ax_topo, ax_colorbar,
    evoked_mean, times, mask, units, scalings, cnorm,
    cmap, show_colorbar=True):
    """
    Plot the topomap for a given cluster or cluster group.
    """
    mne.viz.plot_evoked_topomap(
        evoked_mean,
        times=0,
        mask=mask,
        axes=ax_topo,
        show=False,
        colorbar=False,
        mask_params=dict(markersize=10),
        units=units,
        scalings=scalings,
        cnorm=cnorm,
        cmap=cmap,
    )
    # remove the title that would otherwise say "0.000 s"
    ax_topo.set_title("")
    ax_topo.set_xlabel(f"Averaged t-map ({times[0]:0.3f} - {times[-1]:0.3f} s)")
    # plot colorbar
    image = ax_topo.images[0]
    if show_colorbar:
        plt.colorbar(image, cax=ax_colorbar)
    
def plot_time_courses(ax_signals, evoked, clusters, clu_indices, cluster_pv,
    picks, units, scalings, ylim, highlight_times, title):
    """
    Plot the time courses for a given cluster or cluster group.
    """
    fig = mne.viz.plot_evoked(
        evoked,
        axes=ax_signals,
        units=units,
        scalings=scalings,
        picks=picks,
        titles={"mag": title, "grad": title},
        spatial_colors=True,
        highlight=(highlight_times[0], highlight_times[-1]),
        show=False,
        ylim={"mag": ylim, "grad": ylim},
    )
    ymin, ymax = ax_signals.get_ylim()
    for clu_idx in clu_indices:
        clu_time_inds, clu_ch_inds = np.squeeze(clusters[clu_idx])
        clu_time_inds = np.unique(clu_time_inds)
        clu_ch_inds = np.unique(clu_ch_inds)
        clu_sig_times = evoked.times[clu_time_inds]
        clu_timecourse = evoked.data[clu_ch_inds, :].mean(axis=0)
        is_pos = clu_timecourse[clu_time_inds].mean() > 0
        yline = ymin + (ymax - ymin) * (0.95 if is_pos else 0.05)
        ytext = ymin + (ymax - ymin) * (0.96 if is_pos else 0.04)
        va = "bottom" if is_pos else "top"
        ax_signals.plot([clu_sig_times[0], clu_sig_times[-1]], [yline, yline], '-', color="black", lw=1.)
        ax_signals.text(
            (clu_sig_times[0] + clu_sig_times[-1]) / 2,
            ytext,
            f"p={cluster_pv[clu_idx]:.3f}", fontsize=6,
            ha="center", va=va,
        )
    ax_signals.plot(evoked.times, clu_timecourse, color="black", lw=2)

if __name__ == '__main__':
    main()
