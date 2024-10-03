"""
Estimate the TRFs (temporal response functions) to laser and button events
using example data from the COINS-MEG dataset.

This estimation can be done in source space or sensor space.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import mne
import numpy as np
import osl
import os
import os.path as op

# Utility functions that Cedric likes to use (could be moved to a separate module)
def create_dir_if_needed(d):
    if not op.exists(d):
        os.makedirs(d, exist_ok=True)

def save_figure(fig, figpath, verbose=True):
    fig.savefig(figpath)
    plt.close(fig)
    if verbose:
        print(f"Figure saved at {figpath}")

# Plotting constants and defaults that Cedric likes to use (could be moved to a separate module)
A4_PAPER_CONTENT_WIDTH = 7.1
DEFAULT_HEIGHT = 2.16
def setup_mpl_style(fontsize=8):
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = 'Arial'
    mpl.rcParams['mathtext.default'] = 'regular'
    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['font.size'] = fontsize
    mpl.rcParams['figure.titlesize'] = fontsize
    mpl.rcParams['axes.titlesize'] = fontsize
    mpl.rcParams['axes.labelsize'] = fontsize
    mpl.rcParams['xtick.labelsize'] = fontsize
    mpl.rcParams['ytick.labelsize'] = fontsize
    mpl.rcParams['legend.fontsize'] = fontsize-1
    mpl.rcParams['axes.labelpad'] = 4.0
    mpl.rcParams['lines.linewidth'] = 1.0
    mpl.rcParams["legend.frameon"] = False
    mpl.rcParams['figure.constrained_layout.use'] = True

def main(feat_names=["laserHit", "laserMiss"]):
    # Output directory in which the results will be saved
    outdir = "./gitignore/results"
    create_dir_if_needed(outdir)

    # Local file paths for the example data.
    # Preprocessed, sensor-space MEG data for subject 17 and run 1
    sensorspc_path = "../coins-meg_data/derivatives/preprocessed/sub-17_ses-2-meg_task-coinsmeg_run-1_meg_transsss/sub-17_ses-2-meg_task-coinsmeg_run-1_meg_transsss_preproc_raw.fif"
    # Parcellated, source-space MEG data for subject 17 and run 1 (this file was
    # saved by code in 3_coregister_manual.ipynb)
    sourcespc_path =  '../coins-meg_data/derivatives/src/sub-17/parc_raw.fif'

    # Features (i.e. event types) for which we want to estimate a TRF
    feat_names = ["laserHit", "laserMiss"]
    # feat_names = ["laserHit", "laserMiss", "keyLeft", "keyRight"]

    # Parcel number whose TRF we will want to plot and save.
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
    # Y should be a matrix of shape (n_samples, n_parcels).
    #

    # Create X from stim_data
    X = np.stack([stim_data == f_id for f_id in feat_ids], axis=1) # shape (n_samples, n_features)
    print(f"X shape: {X.shape}")

    # Create Y from parcels_data
    Y = parcels_data.T
    print(f"Y shape: {Y.shape}")

    # Create the TRF model
    trf_model = mne.decoding.ReceptiveField(tmin, tmax, sfreq, feature_names=feat_names)

    # Estimate the TRFs (for all parcels)
    trf_model.fit(X, Y)

    # Extract the TRFs (i.e., the estimated beta coefficients)
    # for the selected parcel
    trfs = trf_model.coef_[i_parcel, :, :]

    #
    # Plot the TRFs of the selected parcels
    #

    setup_mpl_style()
    fig, ax = plt.subplots(figsize=(A4_PAPER_CONTENT_WIDTH / 2, DEFAULT_HEIGHT))
    trf_times = trf_model.delays_ / sfreq
    for i, trf in enumerate(trfs):
        ax.plot(trf_times, trf, '-', label=f"{feat_names[i]}")
    ax.legend()
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Beta coefficient")
    ax.set_title(f"TRFs for parcel {i_parcel}")
    ax.axvline(0, ls=":", color="black")

    # Save the figure
    feat_codes_str = f"feat-{'-'.join([str(id) for id in feat_ids])}"
    figname = f"trf_parcel-{i_parcel}_{feat_codes_str}.png"
    figpath = op.join(outdir, figname)
    save_figure(fig, figpath)

    #
    # Plot the design matrix
    #

    import nilearn.plotting
    import pandas as pd

    # nilearn can plot the design matrix when it is formatted as a dataframe,
    # with columns corresponding features, and rows corresponding to samples.
    design_matrix = pd.DataFrame(X, columns=feat_names)#, index=times)
    figname = f"trf-design-matrix_{feat_codes_str}.png"
    figpath = op.join(outdir, figname)
    ax = nilearn.plotting.plot_design_matrix(design_matrix,)
    fig = ax.get_figure()
    save_figure(fig, figpath)

if __name__ == '__main__':
    main()
