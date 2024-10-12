"""
Estimate the TRFs (temporal response functions) to laser and button events
using example data from the COINS-MEG dataset.

This scripts performs several TRFs estimation using either source space and
sensor space data.
"""

import cf_utils
import coinsmeg_data as coinsmeg
import matplotlib.pyplot as plt
import mne
import numpy as np
import osl
import os.path as op
import sklearn.linear_model

class RidgeWithNan(sklearn.linear_model.Ridge):
    """Subclass of scikit-learn's Ridge estimator that can handle NaN values
    in the data. The strategy for dealing with NaNs is to discard rows
    from X and Y where a NaN value is present in either X or Y."""

    def _nan_rows(self, X):
        if X.ndim == 2:
            return np.isnan(X).any(axis=1)
        elif X.ndim == 1:
            return np.isnan(X)

    def _remove_nan(self, X, Y):
        # Find the row indices where there is a NaN value in either X or Y
        assert X.ndim == 2 and Y.ndim == 2
        nan_rows = self._nan_rows(X) | self._nan_rows(Y)
        # Filter out the rows with NaN values
        X = X[~nan_rows]
        Y = Y[~nan_rows]
        return X, Y

    def fit(self, X, y, sample_weight=None):
        X, y = self._remove_nan(X, y)
        return super().fit(X, y, sample_weight=sample_weight)

    def score(self, X, y, sample_weight=None):
        X, y = self._remove_nan(X, y)
        return super().score(X, y, sample_weight=sample_weight)


def main():
    ########################################################
    # Parameters for the analysis
    ########################################################

     # Subject and run to use for the TRF estimation
    sub = 17
    run = 1

    # Features (i.e. event types) for which we want to estimate a TRF
    feat_names = ["laserHit", "laserMiss"]
    # feat_names = ["keyLeft", "keyRight"]

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
    downsamp_method = "resample"
    downsamp_name = "downsamp" if (downsamp_method == "resample") else "decim"

    # Ridge regularization parameter values to use for the TRF estimation
    alphas = [0]

    # Whether we are running the analysis locally, with a copy of the data
    # stored on our machine, or on the server with access to /ohba/pi/lhunt,
    # where the data is stored.
    do_locally = False
    LOCAL_BASE_DIR = "/Users/cedric/Code_and_Repositories/ContInf_-_Code/coins-meg_data"

    # Whether to plot and save the design matrix
    do_plot_dmtx = False

    # Output directory in which the results will be saved
    # outdir = "./analysis/results"
    outdir = "./gitignore/results"
    cf_utils.create_dir_if_needed(outdir)

    ########################################################
    # Analysis code
    ########################################################

    #
    # File paths to the data for the given subject and run
    #
    paths = {}
    # Preprocessed, sensor-space MEG data
    subdir = f"sub-{sub:02d}_ses-2-meg_task-coinsmeg_run-{run:d}_meg_transsss"
    fname = f"{subdir}_preproc_raw.fif"
    paths['sensorspc'] = op.join(coinsmeg.PREPROCESSED_DIR, subdir, fname)
    # Parcellated, source-space MEG data
    # (this file was created by the code in 3_coregister_manual.ipynb))
    subdir = f"src/sub-{sub:02d}"
    fname = "parc_raw.fif"
    paths["sourcespc"] = op.join(coinsmeg.DERIVATIVES_DIR, subdir, fname)
    if do_locally:
        for k, fpath in paths.items():
            paths[k] = fpath.replace(coinsmeg.BASE_DIR, LOCAL_BASE_DIR)

    # Get event info from the yaml in the preprocessed directory
    sensorspc_dataset = osl.preprocessing.read_dataset(paths["sensorspc"],
        # the ftype parameter below is needed because osl assumes by default
        # that the file should end with 'preproc-raw', rather than 'preproc_raw'
        ftype="preproc_raw")
    event_id = sensorspc_dataset["event_id"]
    feat_ids = [event_id[fn] for fn in feat_names]

    # Get sensor-space and source-space raw objects
    raws = {}
    raws["sensorspc"] = sensorspc_dataset["raw"]
    raws["sourcespc"] = mne.io.read_raw(paths["sourcespc"])

    # Original and new sampling frequency
    original_sfreq = raws["sourcespc"].info["sfreq"]
    sfreq = original_sfreq / downsamp

    # Resample if needed
    if downsamp != 1 and downsamp_method == "resample":
        for k, raw in raws.items():
            raws[k] = raw.resample(sfreq)
        print("Data resampled")

    # Find the indices corresponding to the parcels MEG data vs the stim event channel
    i_all_parcels = mne.pick_types(raws["sourcespc"].info, misc=True)
    i_stim = mne.pick_types(raws["sourcespc"].info, stim=True)[0]

    # Load the MEG data arrays
    data = {}
    reject_by_annotation = None if no_reject else "NaN"
    data["parcels"] = raws["sourcespc"].get_data(i_all_parcels,
        reject_by_annotation=reject_by_annotation) # shape (n_parcels, n_samples)
    data["mag"] = raws["sensorspc"].get_data(picks="mag",
        reject_by_annotation=reject_by_annotation)
    data["grad"] = raws["sensorspc"].get_data(picks="grad",
        reject_by_annotation=reject_by_annotation)

    # Load the stimulus event channel data array
    data["stim"] = raws["sourcespc"].get_data([i_stim],
        reject_by_annotation=reject_by_annotation)[0] # shape (n_samples, )

    #
    # Create X and Y for the TRF estimation
    #
    # X (the design matrix) should be a matrix of shape (n_samples, n_features),
    # where n_features correspond to each event type for which we want to
    # estimate a TRF.
    #
    # Y should be a matrix of shape (n_samples, n_channels) where n_channels
    # corresponds to the number of sensors when working in sensor space, and
    # when working in source space after parcellations, to the number of
    # parcels.
    #

    # Create X from stim data
    X = np.stack([data["stim"] == f_id for f_id in feat_ids],
        axis=1).astype(float) # shape (n_samples, n_features)

    # Create Y from parcels/mag/grad data
    Ys = {}
    for k in ["parcels", "mag", "grad"]:
        Ys[k] = data[k].T
    # Y_parcels = parcels_data.T
    # Y_mag = sensors_data_mag.T
    # Y_grad = sensors_data_grad.T

    # Decimate if needed
    if downsamp != 1 and downsamp_method == "decimate":
        X = X[::downsamp, :]
        for k, Y in Ys.items():
            Ys[k] = Y[::downsamp, :]
        # Y_parcels = Y_parcels[::downsamp, :]
        # Y_mag = Y_mag[::downsamp, :]
        # Y_grad = Y_grad[::downsamp, :]

    print(f"X shape: {X.shape}")
    print(f"""Y parcels shape: {Ys["parcels"].shape}""")
    print(f"""Y mag shape: {Ys["mag"].shape}""")
    print(f"""Y grad shape: {Ys["grad"].shape}""")

    #
    # Plot the design matrix
    #

    cf_utils.setup_mpl_style()

    feats = '-'.join([str(id) for id in feat_ids])

    if do_plot_dmtx:
        import nilearn.plotting
        import pandas as pd
        # nilearn can plot the design matrix when it is formatted as a dataframe,
        # with columns corresponding features, and rows corresponding to samples.
        design_matrix = pd.DataFrame(X, columns=feat_names)#, index=times)
        figname = cf_utils.name_with_params("trf-design-matrix",
            # ["sub", "run", "feats"], [sub, run, feats]
            ["sub", "run", "feats", downsamp_name], [sub, run, feats, downsamp])
        figpath = cf_utils.path_with_components(outdir, figname, "png")
        ax = nilearn.plotting.plot_design_matrix(design_matrix,
            # rescale=False
            )
        fig = ax.get_figure()
        cf_utils.save_figure(fig, figpath)

    #
    # Estimate the TRFs
    #

    for k, Y in Ys.items():
        space = "source" if k == "parcels" else "sensor"
        pick = f"parcel-{i_parcel}" if k == "parcels" else k

        for alpha in alphas:
            # Create the TRF model
            estimator = (alpha if no_reject else RidgeWithNan(
                alpha=alpha, fit_intercept=True))
            trf_model = mne.decoding.ReceptiveField(tmin, tmax, sfreq,
                feature_names=feat_names, estimator=estimator)

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
                trfs = np.sqrt((trf_model.coef_ ** 2).mean(axis=0))
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
                    ax.plot(trf_times[start:end], trf[start:end], '-', label=f"{feat_names[i]}")
                ax.legend()
                ax.set_xlabel("Time (s)")
                ax.set_ylabel("Beta coefficient")
                ax.set_title(title)
                ax.axvline(0, ls=":", color="black")

                # Save the figure
                windowstr = f"{window[0]}-{window[1]}" if window else None
                figname = cf_utils.name_with_params("trf",
                    ["sub", "run", "space", "pick", "feats", downsamp_name, "alpha", "no-reject",  "window"],
                    [sub, run, space, pick, feats, downsamp, alpha, no_reject, windowstr]
                    )
                figpath = cf_utils.path_with_components(outdir, figname, "png")
                cf_utils.save_figure(fig, figpath)

if __name__ == '__main__':
    main()
