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

    # dont_recompute: If True, the TRFs are loaded from the results of
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
    downsamp = args.downsamp # default: 10

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
    # Whether to save the TRFs.
    do_save_trfs = True
    # Whether to plot the TRFs.
    do_plot_trfs = True

    # Output directory in which the results will be saved
    outdir_parent = "./gitignore/results"

    ########################################################
    # Analysis code
    ########################################################

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

        # File path where the TRFs are saved
        trf_fpath = {}
        for k in datatypes:
            paramkeys = ["sub", "events", "datatype", downsamp_name, "alpha", "no-reject"]
            paramvals = [sub, events, k, downsamp, alpha, no_reject]
            trf_fname = cf_utils.name_with_params("trfs", paramkeys, paramvals)
            trf_fname += "_ave" # MNE recommends the file name to end with "ave" for evoked instances
            trf_fpath[k] = cf_utils.path_with_components(outdir, trf_fname, "fif")
        
        #
        # Load the TRFs if dont_recompute is True and they have been saved
        # from an earlier run
        #
        trfsdict = {}
        if dont_recompute and all([op.exists(f) for f in trf_fpath.values()]):
            for k, f in trf_fpath.items():
                trfsdict[k] = cf_trf.load_trfs(f)

        #
        # Compute the TRFs otherwise
        #
        else:
            # Compute the X and Y matrices for the TRF estimation
            XY = cf_trf.get_XY(sub, event_names, do_locally=do_locally,
            tmin=tmin, tmax=tmax, downsamp=downsamp, downsamp_method=downsamp_method,
            no_reject=no_reject, spaces=spaces)
            X = XY["X"]
            Ys = XY["Y"]
            # Plot the design matrix (X) if needed
            if do_plot_dmtx:
                ax = cf_trf.plot_design_matrix(X, event_names)
                figname = cf_utils.name_with_params("trf-design-matrix",
                    ["sub", "events", downsamp_name], [sub, events, downsamp])
                figpath = cf_utils.path_with_components(outdir, figname, "png")
                fig = ax.get_figure()
                cf_utils.save_figure(fig, figpath)
            if args.do_only_dmtx:
                continue
            # Compute the TRFs from the X and Y matrices
            for k, Y in Ys.items():
                Y_info = XY["Y_info"][k]
                sfreq = Y_info["sfreq"]
                # Create the TRF model
                trf_model = cf_trf.create_trf_model(event_names, sfreq,
                    tmin=tmin, tmax=tmax, no_reject=no_reject, alpha=alpha)
                # Estimate the TRFs
                trfsdict[k] = cf_trf.estimate_trfs(trf_model, X, Y, Y_info)
                # Save the TRFs
                if do_save_trfs:
                    cf_trf.save_trfs(trfsdict[k], trf_fpath[k])

        #
        # Plot the TRFs
        #
        if do_plot_trfs:
            for k, trfs in trfsdict.items():
                space = "source" if k == "parcels" else "sensor"
                if space == "source":
                    picks = ["all", 2]
                else:
                    picks = [k]

                for pick in picks:
                    title = f"TRF, {space} space"
                    if space == "source":
                        title += f", all parcels" if pick == "all" else f", parcel {pick}"
                    else:
                        title += f", {pick}"
                    agg = None if type(pick) == int else "rms" 
                    ylabel = "RMS amplitude" if agg == "rms" else "Beta coefficient"

                    fig, ax = plt.subplots(figsize=(cf_utils.A4_PAPER_CONTENT_WIDTH / 2,
                                                cf_utils.DEFAULT_HEIGHT))
                    if agg == "rms":
                        # Calculate and plot the RMS across channels (sensors/parcels)
                        # of the TRF beta coefficients
                        for i_ev, trf_inst in enumerate(trfs):
                            rms = cf_trf.calculate_rms_trf(trf_inst.data)
                            ax.plot(trf_inst.times, rms.T, '-',
                                    label=f"{event_names[i_ev]}")
                    else:
                        # Plot the TRF beta coefficients for the given picked channel
                        for i_ev, trf_inst in enumerate(trfs):
                            ax.plot(trf_inst.times, trf_inst.data[pick, :], '-',
                                    label=f"{event_names[i_ev]}")
                    ax.legend()
                    ax.set_xlabel("Time (s)")
                    ax.set_ylabel(ylabel)
                    ax.set_title(title)
                    ax.axvline(0, ls=":", color="black")

                    # Save the figure
                    figname = cf_utils.name_with_params("trf-plot",
                        ["sub", "events", "space", "pick", "agg", downsamp_name, "alpha", "no-reject"],
                        [sub, events, space, pick, agg, downsamp, alpha, no_reject])
                    figpath = cf_utils.path_with_components(outdir, figname, "png")
                    cf_utils.save_figure(fig, figpath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dont_recompute", action='store_true', default=False)
    parser.add_argument("--do_only_dmtx", action='store_true', default=False)
    parser.add_argument("--downsamp", type=int, default=10)
    parser.add_argument("-ev", "--events", nargs="+", type=str,
        default=["laserHit", "laserMiss"])
    args = parser.parse_args()
    main(args)
