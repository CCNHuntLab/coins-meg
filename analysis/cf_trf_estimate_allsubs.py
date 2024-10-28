"""
Estimate the TRFs (temporal response functions) to events at the subject level,
for all subjects.
"""

import argparse
import cf_utils
import cf_trf
import coinsmeg_data as coinsmeg
import numpy as np
import matplotlib.pyplot as plt
import os.path as op

def main(args):
    ########################################################
    # Parameters for the analysis
    ########################################################

    # dont_recompute: If True, the TRF estimates are loaded from the results of
    # an earlier run rather than recomputed, if such results are available.
    dont_recompute = args.dont_recompute

    # Names of the events for which we want to estimate a TRF 
    event_names = args.events # default: ["laserHit", "laserMiss"]
    events = '-'.join([str(coinsmeg.EVENT_ID[ev]) for ev in event_names])

    # Time window for the TRF
    tmin = -0.5
    tmax = 1.0

    # Whether to reject or skip rejecting bad segments, as defined by annotations
    no_reject = False

    # Downsampling factor to use for the TRF estimation
    downsamp = 10

    # Method to downsample: "resample" or "decimate"
    # downsamp_method = "resample"
    downsamp_method = "decimate"
    downsamp_name = "downsamp" if (downsamp_method == "resample") else "decim"

    # Ridge regularization parameter values to use for the TRF estimation
    alpha = 0

    # Whether we are running the analysis locally, with a copy of the data
    # stored on our machine, or on the server with access to /ohba/pi/lhunt,
    # where the data is stored.
    do_locally = False

    # Whether to plot and save the design matrix
    do_plot_dmtx = True
    # Whether to save the TRF model estimates (beta coefficient)
    do_save_trfs = True
    # Whether to plot the TRFs. In source space, this will plot the TRF on a
    # per-parcel basis. In sensor-space, this will plot the average amplitude
    # (root mean square) of the TRFs across sensors.
    do_plot_trfs = True

    # Output directory in which the results will be saved
    outdir_parent = "./gitignore/results"
    cf_utils.create_dir_if_needed(outdir_parent)

    cf_utils.setup_mpl_style()

    for sub in coinsmeg.SUB_NUMS_ALL:
        print(f"Running subject {sub}")

        outdir = op.join(outdir_parent, coinsmeg.sub_num2str(sub))
        cf_utils.create_dir_if_needed(outdir)

        # Skip source-space/sensor-space analysis if we don't have
        # all the source-space/sensor-space data for this subject
        spaces = []
        datatypes = []
        # sensorspc_data_paths = [cf_utils.get_path_for_data(
        #     coinsmeg.get_sub_preproc_raw_fpath(sub, run), do_locally) for run in coinsmeg.RUNS]
        # sourcespc_data_paths = [cf_utils.get_path_for_data(
        #     coinsmeg.get_sub_src_parc_fpath(sub, run), do_locally) for run in coinsmeg.RUNS]
        has_all_sensorspc_data = all([op.exists(cf_utils.get_path_for_data(
            coinsmeg.get_sub_preproc_raw_fpath(sub, run), do_locally)) for run in coinsmeg.RUNS])
        has_all_sourcespc_data = all([op.exists(cf_utils.get_path_for_data(
            coinsmeg.get_sub_src_parc_fpath(sub, run), do_locally)) for run in coinsmeg.RUNS])
        if has_all_sensorspc_data:
            spaces += ["sensor"]
            datatypes += ["mag", "grad"]
        if has_all_sourcespc_data:
            spaces += ["source"]
            datatypes += ["parcels"]

        if len(spaces) == 0 or len(datatypes) == 0:
            print("Skipping this subject because we don't have all the data")
            continue

    ########################################################
    # Analysis code
    ########################################################
        # File path where the TRF estimates are saved
        trf_fpath = {}
        for k in datatypes:
            paramkeys = ["sub", "datatype", "events", downsamp_name, "alpha", "no-reject"]
            paramvals = [sub, k, events, downsamp, alpha, no_reject]
            trf_fname = cf_utils.name_with_params("trf", paramkeys,paramvals)
            trf_fpath[k] = cf_utils.path_with_components(outdir, trf_fname, "npy")
        trf_times_fname = cf_utils.name_with_params("trf-times",
                ["tmin", "tmax", downsamp_name], [tmin, tmax, downsamp])
        trf_times_fpath = cf_utils.path_with_components(outdir, trf_times_fname, "npy")
        
        # Load the TRF estimates if dont_recompute is True and they have been saved
        # from an earlier run
        trf = {}
        trf_times = None
        if dont_recompute and all([op.exists(f) for f in trf_fpath.values()]):
            for k, f in trf_fpath.items():
                trf[k] = np.load(f)
            trf_times = np.load(trf_times_fpath)

        # Compute the TRF estimates otherwise
        else:
            # Compute the X and Y matrices for the TRF estimation
            XY = cf_trf.get_XY(sub, event_names, do_locally=do_locally,
            tmin=tmin, tmax=tmax, downsamp=downsamp, downsamp_method=downsamp_method,
            no_reject=no_reject, spaces=spaces)
            X = XY["X"]
            Ys = XY["Y"]
            sfreq = XY["sfreq"]
            # Plot the design matrix (X) if needed
            if do_plot_dmtx:
                ax = cf_trf.plot_design_matrix(X, event_names)
                figname = cf_utils.name_with_params("trf-design-matrix",
                    ["sub", "events", downsamp_name], [sub, events, downsamp])
                figpath = cf_utils.path_with_components(outdir, figname, "png")
                fig = ax.get_figure()
                cf_utils.save_figure(fig, figpath)
            # Estimate the TRFs
            for k, Y in Ys.items():
                # Create the TRF model
                trf_model = cf_trf.create_trf_model(event_names, sfreq,
                    tmin=tmin, tmax=tmax, no_reject=no_reject, alpha=alpha)
                # Estimate and extract the TRF model coefficients
                trf_model.fit(X, Y)
                trf[k] = trf_model.coef_
                if trf_times is None:
                    trf_times = trf_model.delays_ / sfreq
            # Save the TRFs
            if do_save_trfs:
                for k in trf.keys():
                    np.save(trf_fpath[k], trf[k])
                    print(f"TRFs for {k} saved at {trf_fpath[k]}")
                np.save(trf_times_fpath, trf_times)
                print(f"TRF times saved at {trf_times_fpath}")

        #
        # Plot the TRFs
        #
        if do_plot_trfs:
            for k, trfs in trf.items():
                space = "source" if k == "parcels" else "sensor"
                if space == "source":
                    picks = ["all", 2]
                else:
                    # In sensor space:
                    # Calculate the RMS across sensors of the beta coefficients
                    picks = [k]

                for pick in picks:
                    title = f"TRF, {space} space"
                    if space == "source":
                        title += f", all parcels" if pick == "all" else f", parcel {pick}"
                    else:
                        title += f", {pick}"
                    ylabel = "Beta coefficient" if space == "source" else "RMS amplitude"

                    fig, ax = plt.subplots(figsize=(cf_utils.A4_PAPER_CONTENT_WIDTH / 2,
                                                cf_utils.DEFAULT_HEIGHT))
                    if space == "source":
                        # In source space:
                        # Plot all parcels in one figure,
                        # and plot a specific parcel on another figure
                        if pick == "all":
                            cmap = plt.get_cmap('tab10')
                            for i_ev in range(trfs.shape[1]):
                                ax.plot(trf_times, trfs[0, i_ev, :], '-',
                                    label=f"{event_names[i_ev]}",
                                    color=cmap(i_ev))
                                ax.plot(trf_times, trfs[1:, i_ev, ].T, '-',
                                    color=cmap(i_ev))
                        else:
                            for i_ev in range(trfs.shape[1]):
                                ax.plot(trf_times, trfs[pick, i_ev, :], '-',
                                    label=f"{event_names[i_ev]}")
                    else:
                        # In sensor space:
                        # Calculate the RMS across sensors of the beta coefficients
                        trfs_rms = cf_trf.calculate_rms_trf(trfs)
                        for i_ev in range(trfs_rms.shape[0]):
                                ax.plot(trf_times, trfs_rms[i_ev, :].T, '-',
                                    label=f"{event_names[i_ev]}")

                    ax.legend()
                    ax.set_xlabel("Time (s)")
                    ax.set_ylabel(ylabel)
                    ax.set_title(title)
                    ax.axvline(0, ls=":", color="black")
                    

                    # Save the figure
                    figname = cf_utils.name_with_params("trf-plot",
                        ["sub", "space", "pick", "events", downsamp_name, "alpha", "no-reject"],
                        [sub, space, pick, events, downsamp, alpha, no_reject])
                    figpath = cf_utils.path_with_components(outdir, figname, "png")
                    cf_utils.save_figure(fig, figpath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dont_recompute", action='store_true', default=False)
    parser.add_argument("-ev", "--events", nargs="+", type=str,
        default=["laserHit", "laserMiss"])
    args = parser.parse_args()
    main(args)
