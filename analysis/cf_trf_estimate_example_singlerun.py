"""
Estimate the TRFs (temporal response functions) to events for a given run and subject.

This scripts performs separate TRFs estimation for each type of MEG data:
parcellated source-space data ('parcels'), sensor-space magnetometer data ('mag'),
and sensor-space gradiometer data ('grad').
"""

import cf_utils
import cf_trf
import coinsmeg_data as coinsmeg
import matplotlib.pyplot as plt


def main():
    ########################################################
    # Parameters for the analysis
    ########################################################

    # Subject and run to use for the TRF estimation
    sub = 17
    run = 1

    # Names of the events for which we want to estimate a TRF 
    event_names = ["laserHit", "laserMiss"]
    # event_names = ["keyLeft", "keyRight"]

    # Time window for the TRF
    tmin = -0.5
    tmax = 1.0

    # Parcel number whose TRF we will plot and save, when estimating in source space.
    i_parcel = 2

    # Whether to reject or skip rejecting bad segments, as defined by annotations
    no_reject = False

    # Downsampling factor to use for the TRF estimation (this saves memory and
    # compute time, but also improves statistical estimation due to decreasing
    # the number of beta coefficients to estimate)
    downsamp = 10

    # Method to downsample: "resample" or "decimate"
    # downsamp_method = "resample"
    downsamp_method = "decimate"
    downsamp_name = "downsamp" if (downsamp_method == "resample") else "decim"

    # Ridge regularization parameter values to use for the TRF estimation
    alphas = [0]

    # Whether we are running the analysis locally, with a copy of the data
    # stored on our machine, or on the server with access to /ohba/pi/lhunt,
    # where the data is stored.
    do_locally = False

    # Whether to plot and save the design matrix
    do_plot_dmtx = True

    # Output directory in which the results will be saved
    # outdir = "./analysis/results"
    outdir = "./gitignore/results"
    cf_utils.create_dir_if_needed(outdir)

    ########################################################
    # Analysis code
    ########################################################

    XY = cf_trf.get_XY_singlerun(sub, run, event_names, do_locally=do_locally,
        tmin=tmin, tmax=tmax, downsamp=downsamp, downsamp_method=downsamp_method,
        no_reject=no_reject)
    X = XY["X"]
    Ys = XY["Y"]

    print(f"X shape: {X.shape}")
    print(f"""Y parcels shape: {Ys["parcels"].shape}""")
    print(f"""Y mag shape: {Ys["mag"].shape}""")
    print(f"""Y grad shape: {Ys["grad"].shape}""")

    #
    # Plot the design matrix
    #

    cf_utils.setup_mpl_style()

    events = '-'.join([str(coinsmeg.EVENT_ID[ev]) for ev in event_names])

    if do_plot_dmtx:
        ax = cf_trf.plot_design_matrix(X, event_names)
        fig = ax.get_figure()
        figname = cf_utils.name_with_params("trf-design-matrix",
            ["sub", "run", "events", downsamp_name], [sub, run, events, downsamp])
        figpath = cf_utils.path_with_components(outdir, figname, "png")
        cf_utils.save_figure(fig, figpath)

    #
    # Estimate the TRFs
    #

    for k, Y in Ys.items():
        space = "source" if k == "parcels" else "sensor"
        pick = f"parcel-{i_parcel}" if k == "parcels" else k
        sfreq = XY["Y_info"][k]["sfreq"]

        for alpha in alphas:
            # Create the TRF model
            trf_model = cf_trf.create_trf_model(event_names, sfreq,
                tmin=tmin, tmax=tmax, no_reject=no_reject, alpha=alpha)

            # Estimate the TRFs
            trf_model.fit(X, Y)

            # Extract the summary TRF to plot based on the estimated TRFs
            if space == "source":
                # In source space:
                # Extract the estimated beta coefficients
                # for the selected parcel.
                trfs = trf_model.coef_[i_parcel, :, :]
                title = f"TRFs for parcel {i_parcel} in {space} space"
            else:
                # In sensor space:
                # Calculate the RMS across sensors of the beta coefficients,
                # to mirror the behavior of mne.viz.plot_compare_evokeds(),
                # so that we can compare with Epoched ERFs.
                trfs = cf_trf.calculate_rms_trf(trf_model.coef_)
                title = f"TRFs for {pick} sensors (RMS amplitude)"
            #
            # Plot the TRFs
            #

            for window in [None, 
                # (tmin+1/sfreq, tmax-1/sfreq)
                ]:
                fig, ax = plt.subplots(figsize=(cf_utils.A4_PAPER_CONTENT_WIDTH / 2,
                                                cf_utils.DEFAULT_HEIGHT))
                trf_times = trf_model.delays_ / sfreq
                start = (int((window[0]-tmin) * sfreq)
                            if window is not None
                            else 0)
                end = (int((trf_times.shape[0] - (tmax-window[1]) * sfreq))
                    if window is not None
                    else trf_times.shape[0])
                for i, trf in enumerate(trfs):
                    ax.plot(trf_times[start:end], trf[start:end], '-', label=f"{event_names[i]}")
                ax.legend()
                ax.set_xlabel("Time (s)")
                ax.set_ylabel("Beta coefficient")
                ax.set_title(title)
                ax.axvline(0, ls=":", color="black")

                # Save the figure
                windowstr = f"{window[0]}-{window[1]}" if window else None
                figname = cf_utils.name_with_params("trf",
                    ["sub", "run", "events", "space", "pick", downsamp_name, "alpha", "no-reject",  "window"],
                    [sub, run, events, space, pick, downsamp, alpha, no_reject, windowstr]
                    )
                figpath = cf_utils.path_with_components(outdir, figname, "png")
                cf_utils.save_figure(fig, figpath)

if __name__ == '__main__':
    main()
