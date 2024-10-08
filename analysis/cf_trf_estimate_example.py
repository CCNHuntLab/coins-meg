"""
Estimate the TRFs (temporal response functions) to laser and button events
using example data from the COINS-MEG dataset.

This estimation can be done in source space or sensor space.
"""

import cf_utils
import matplotlib.pyplot as plt
import mne
import numpy as np
import osl
import os.path as op

def main():
    # Features (i.e. event types) for which we want to estimate a TRF
    feat_names = ["laserHit", "laserMiss"]
    # feat_names = ["laserHit", "laserMiss", "keyLeft", "keyRight"]

    # Output directory in which the results will be saved
    outdir = "./gitignore/results"
    cf_utils.create_dir_if_needed(outdir)

    # Local file paths for the example data.
    # Preprocessed, sensor-space MEG data for subject 17 and run 1
    sensorspc_path = "../coins-meg_data/derivatives/preprocessed/sub-17_ses-2-meg_task-coinsmeg_run-1_meg_transsss/sub-17_ses-2-meg_task-coinsmeg_run-1_meg_transsss_preproc_raw.fif"
    # Parcellated, source-space MEG data for subject 17 and run 1 (this file was
    # saved by code in 3_coregister_manual.ipynb)
    sourcespc_path =  '../coins-meg_data/derivatives/src/sub-17/parc_raw.fif'
    
    # Subject and run corresponding to this example
    sub = 17
    run = 1

    # Parcel number whose TRF we will plot and save.
    i_parcel = 2

    # Time window for the TRF
    tmin = -0.5
    tmax = 1.0

    # Get event info from the yaml in the preprocessed directory
    sensorspc_dataset = osl.preprocessing.read_dataset(sensorspc_path,
        # the below argument is needed because osl assumes by default that the file
        # should end with 'preproc-raw' rather than 'preproc_raw'
        ftype="preproc_raw")
    event_id = sensorspc_dataset["event_id"]
    feat_ids = [event_id[fn] for fn in feat_names]

    # Load the sensor-space data
    sensorspc_raw = sensorspc_dataset["raw"]
    sensors_data_mag = sensorspc_raw.get_data(picks="mag")
    sensors_data_grad = sensorspc_raw.get_data(picks="grad")

    # Load the source-space data
    sourcespc_raw = mne.io.read_raw(sourcespc_path)

    # Find the indices corresponding to the parcels MEG data vs the stim event channel
    i_all_parcels = mne.pick_types(sourcespc_raw.info, misc=True)
    i_stim = mne.pick_types(sourcespc_raw.info, stim=True)[0]

    # Load the MEG data array for each parcel
    parcels_data = sourcespc_raw.get_data(i_all_parcels) # shape (n_parcels, n_samples)

    # Load the stimulus event channel
    stim_data = sourcespc_raw.get_data([i_stim])[0] # shape (n_samples, )

    # Sampling frequency
    sfreq = sourcespc_raw.info["sfreq"]

    # Uncomment the line below to get the time of each sample
    # _, times = sourcespc_raw.get_data(picks=[0], return_times=True)

    #
    # Create X and Y for the TRF estimation
    #
    # X should be a matrix (called the design matrix)
    # of shape (n_samples, n_features), where n_features correspond to each event type
    # for which we want to estimate a TRF.
    #
    # Y should be a matrix of shape (n_samples, n_channels) where
    # n_channels corresponds to the number of sensors when working in sensor space,
    # and when working in source space after parcellations, to the number of parcels.
    #

    # Create X from stim_data
    X = np.stack([stim_data == f_id for f_id in feat_ids], axis=1) # shape (n_samples, n_features)
    print(f"X shape: {X.shape}")

    # Create Y from parcels_data / sensors_data
    Y_parcels = parcels_data.T
    Y_mag = sensors_data_mag.T
    Y_grad = sensors_data_grad.T
    print(f"Y_parcels shape: {Y_parcels.shape}")
    print(f"Y_mag shape: {Y_mag.shape}")
    print(f"Y_grad shape: {Y_grad.shape}")

    #
    # Plot the design matrix
    #

    cf_utils.setup_mpl_style()

    import nilearn.plotting
    import pandas as pd

    # nilearn can plot the design matrix when it is formatted as a dataframe,
    # with columns corresponding features, and rows corresponding to samples.
    design_matrix = pd.DataFrame(X, columns=feat_names)#, index=times)
    feats = '-'.join([str(id) for id in feat_ids])
    figname = cf_utils.name_with_params("trf-design-matrix",
        ["sub", "run", "feats"], [sub, run, feats])
    figpath = cf_utils.path_with_components(outdir, figname, "png")
    ax = nilearn.plotting.plot_design_matrix(design_matrix,)
    fig = ax.get_figure()
    cf_utils.save_figure(fig, figpath)

    for (Y, space, pick) in [(Y_parcels, "source", f"parcel-{i_parcel}"),
        (Y_mag, "sensor", "mag"), (Y_grad, "sensor", "grad")]:
    # for (Y, space, pick) in [(Y_parcels, "source", f"parcel-{i_parcel}")]:

        # Create the TRF model
        trf_model = mne.decoding.ReceptiveField(tmin, tmax, sfreq, feature_names=feat_names)

        # Estimate the TRFs (for all parcels)
        trf_model.fit(X, Y)

        if space == "source":
            # In source space:
            # Extract the TRFs (i.e., the estimated beta coefficients)
            # for the selected parcel
            trfs = trf_model.coef_[i_parcel, :, :]
            title = f"TRFs for parcel {i_parcel} in {space} space"
        else:
            # In sensor space:
            # Calculate the Root-mean-square amplitude across the sensors to mirror
            # the behavior of mne.viz.plot_compare_evokeds()
            trfs = np.sqrt((trf_model.coef_ ** 2).mean(axis=0))
            title = f"TRFs for {pick} sensors (mean RMS amplitude across sensors)"
        #
        # Plot the TRFs of the selected parcels
        #

        for window in [None, (-0.4, 0.9)]:
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
                ["sub", "run", "space", "pick", "feats", "window"],
                [sub, run, space, pick, feats, windowstr])
            figpath = cf_utils.path_with_components(outdir, figname, "png")
            cf_utils.save_figure(fig, figpath)

if __name__ == '__main__':
    main()
