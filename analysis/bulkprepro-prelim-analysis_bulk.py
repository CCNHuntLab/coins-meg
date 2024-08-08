# Preliminary Analysis with Maxfiltered and Bulk-Preprocessed Data

##### Last edited AXL 23/10/23

# This script contains some preliminary 'analyses'/visualisation of the COINS-MEG MEG data. 
# The inputted data is the maxfiltered and bulk-preprocessed version. 
# The script takes in the subject number & runs specified in "sub_run_pairs", and automatically runs
# the visualisation code and saves plots in the corresponding subject folder -- in the path
# preprocessed/sub-{subj}/run-{run}/meg/auto-max/plots

# Load packages

from matplotlib import pyplot as plt

import mne
import osl
import numpy as np
import os

from pprint import pprint
import glob
import pandas as pd
from mne.preprocessing import create_eog_epochs, create_ecg_epochs
import matplotlib
matplotlib.rcParams.update({'font.size': 14}) # set font size for plots
matplotlib.use('Agg') # suppress plot pop-ups

# Read in the data ####
basedir = '/Volumes/external-drive/work-data/coins-meg_meg-analysis/'
#basedir = '/Users/amyli/Desktop/LH-lab/coins-meg_meg-analysis/'
#basedir = '/ohba/pi/lhunt/datasets/coins-meg_meg-analysis'
#sub_run_pairs = [['11', '1'], ['04', '2'], ['10', '2'], ['10', '3'], ['04', '3'], ['10', '2'], ['10', '3'], ['04', '3'], ['12', '4'], ['04', '1']]
sub_run_pairs = [['18', '4']]

ifMaxfiltered = True # set to true so that directories point to maxfiltered data

for n_sub_run in range(len(sub_run_pairs)):
    subj = sub_run_pairs[n_sub_run][0]
    run = sub_run_pairs[n_sub_run][1]

    # Set directory paths
    procdir = os.path.join(basedir, 'preprocessed') # directory for the processed data

    dir_meg = os.path.join(procdir, f'sub-{subj}', f'run-{run}', 'meg', 'auto-max')  # folder where auto-preproc, maxfiltered versions live

    dir_meg_derivatives = os.path.join(dir_meg, 'derivatives') # for storing derivatives from processing (eg fif files)
    dir_meg_plots = os.path.join(dir_meg, 'plots') # for storing plots generated during preprocessing

    # generate the output directory if it doesn't exist

    os.makedirs(dir_meg_derivatives, exist_ok=True)
    os.makedirs(dir_meg_plots, exist_ok=True)

    preproc_fname = os.path.join(procdir, 'auto-max', 'auto-max', f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss',
                                     f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss_preproc_raw.fif')
    ica_fname = os.path.join(procdir, 'auto-max', 'auto-max', f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss',
                                     f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss_ica.fif')

    # Now actually read in the preprocessed and ica data
    clean = mne.io.read_raw_fif(preproc_fname, preload=True)

    # Additional bandpassing for purpose of ERFs
    #clean_bp = clean.copy()
    clean_bp = clean.copy().filter(l_freq=0.25, h_freq=30) # suggested to set l_freq to 1.0 for ICA
    #clean_bp.save(os.path.join(dir_meg_derivatives, 'clean_bp.fif'))

    ica = mne.preprocessing.read_ica(ica_fname)

    # Laser Hit vs Miss Visualisation ####

    ## Define and process epochs ####

    # Define the events
    events = mne.find_events(clean_bp, min_duration=0.005)
    event_color = {}
    event_dict = {'laserHit': 1, 'laserMiss': 2, 'keyRight': 3, 'keyLeft': 4, 'keyUp': 5, 'keyDown': 6, 'keyRelease': 7}

    # Create epochs (-0.5 to 1.0s epoch around event)
    epochs = mne.Epochs(clean_bp, events, tmin=-0.5, tmax=1.0, event_id=event_dict) # -0.5-1.0

    # Remove epochs with particularly high peak-to-peak amplitudes, as this indicates there might still
    # be segments in the data with high variance, that we didn't find earlier. We also include EOG peak-to-peak
    # amplitude, as high amplitudes indicate saccades.
    epochs.drop_bad({"eog": 6e-4, "mag": 4e-11, "grad": 4e-10}) # defines specific thresholds for peak-to-peak amplitudes in different types of channels

    # Plot % of epochs dropped
    epochs.plot_drop_log()
    plt.savefig(os.path.join(dir_meg_plots, 'epoch-drop_-0.5-1.0.png'), format='png')

    # Use equalize_event_counts() to randomly sample epochs from each condition to match the number
    # of epochs present in the condition w/ the fewest good epochs
    conditions = ["laserHit", "laserMiss"]
    epochs.equalize_event_counts(conditions)

    hit_epochs = epochs["laserHit"]
    miss_epochs = epochs["laserMiss"]

    ## Visualise ERFs ####
    # Compute average evoked responses for hit and miss epochs
    ## hit ERFs
    evoked_hit = hit_epochs.average()

    fig = evoked_hit.plot_joint(picks='mag')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_laserHit.png'), format='png')

    fig = evoked_hit.plot_joint(picks='grad')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_laserHit.png'), format='png')

    ## miss ERFs
    evoked_miss = miss_epochs.average()

    fig = evoked_miss.plot_joint(picks='mag')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_laserMiss.png'), format='png')

    fig = evoked_miss.plot_joint(picks='grad')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_laserMiss.png'), format='png')

    ## Compare hit vs miss evokeds

    mne.viz.plot_compare_evokeds([evoked_hit, evoked_miss], picks='mag',
                                 show_sensors='upper right')
    plt.savefig(os.path.join(dir_meg_plots, 'erf-mag-gfp_hitVsMiss.png'), format='png')

    mne.viz.plot_compare_evokeds([evoked_hit, evoked_miss], picks='grad',
                                 show_sensors='upper right')
    plt.savefig(os.path.join(dir_meg_plots, 'erf-grad-gfp_hitVsMiss.png'), format='png')

    ## difference waveform hit-miss
    evokeds_diff_hitVsMiss = mne.combine_evoked([evoked_hit, evoked_miss], weights=[1, -1])
    fig = evokeds_diff_hitVsMiss.plot_joint(picks='mag')
    fig.set_size_inches((11, 7))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-mag_hitVsMiss.png'), format='png')
    fig = evokeds_diff_hitVsMiss.plot_joint(picks='grad')
    fig.set_size_inches((11, 7))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-grad_hitVsMiss.png'), format='png')

    # Key Left vs Right Visualisation ####

    ## Define and process epochs ####
    # Create epochs for movement keys (left vs right); no baselining applied

    epochs = mne.Epochs(clean_bp, events, baseline=None, tmin=-3.0, tmax=1.0, event_id=event_dict) # different epoch times now compared to hit/miss
    print(epochs)

    # Remove epochs with particularly high peak-to-peak amplitudes, as we did for hit/miss epochs

    epochs.drop_bad({"eog": 6e-4, "mag": 4e-11, "grad": 4e-10}) # defines specific thresholds for peak-to-peak amplitudes in different types of channels
    epochs.plot_drop_log()
    plt.savefig(os.path.join(dir_meg_plots, 'epoch-drop_-3.0-1.0.png'), format='png')

    # use equalize_event_counts first to randomly sample epochs from each condition to match the number
    # of epochs present in the condition w/ the fewest good epochs
    conditions = ["keyLeft", "keyRight"]
    epochs.equalize_event_counts(conditions)

    left_epochs = epochs["keyLeft"]
    right_epochs = epochs["keyRight"]

    # Compute average evoked responses for left and right epochs

    evoked_left = left_epochs.average()
    fig = evoked_left.plot_joint(picks='mag')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_keyLeft.png'), format='png')
    fig = evoked_left.plot_joint(picks='grad')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_keyLeft.png'), format='png')

    evoked_right = right_epochs.average()
    fig = evoked_right.plot_joint(picks='mag')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_keyRight.png'), format='png')
    fig = evoked_right.plot_joint(picks='grad')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_keyRight.png'), format='png')

    # Compare left vs right evokeds

    ## Plot GFP for both mag and grad sensors
    mne.viz.plot_compare_evokeds([evoked_left, evoked_right], picks='mag',
                                 show_sensors='upper right')
    plt.savefig(os.path.join(dir_meg_plots, 'erf-mag-gfp_leftVsRight.png'), format='png')
    mne.viz.plot_compare_evokeds([evoked_left, evoked_right], picks='grad',
                                 show_sensors='upper right');
    plt.savefig(os.path.join(dir_meg_plots, 'erf-grad-gfp_leftVsRight.png'), format='png')

    ## difference waveform left-right; all sensors + topography

    evokeds_diff_leftVsRight = mne.combine_evoked([evoked_left, evoked_right], weights=[1, -1])
    fig = evokeds_diff_leftVsRight.plot_joint(picks='mag')
    fig.set_size_inches((11, 7))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-mag_leftVsRight.png'), format='png')
    fig = evokeds_diff_leftVsRight.plot_joint(picks='grad')
    fig.set_size_inches((11, 7))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-grad_leftVsRight.png'), format='png')

    # Shield Size Up vs Down Visualisation ####

    # Don't need to redefine epochs; used the previous non-baselined ones again from keyleft vs right

    # use equalize_event_counts first to randomly sample epochs from each condition to match the number
    # of epochs present in the condition w/ the fewest good epochs
    conditions = ["keyUp", "keyDown"]
    epochs.equalize_event_counts(conditions)

    up_epochs = epochs["keyUp"]
    down_epochs = epochs["keyDown"]

    ### Visualising Evoked Potentials for keyUp

    # Compute average evoked responses for up and down epochs

    evoked_up = up_epochs.average()

    fig = evoked_up.plot_joint(picks='mag')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_keyUp.png'), format='png')
    fig = evoked_up.plot_joint(picks='grad')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_keyUp.png'), format='png')

    evoked_down = down_epochs.average()

    fig = evoked_down.plot_joint(picks='mag')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_keyDown.png'), format='png')
    fig = evoked_down.plot_joint(picks='grad')
    fig.set_size_inches((9, 6))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_keyDown.png'), format='png')

    mne.viz.plot_compare_evokeds([evoked_up, evoked_down], picks='mag',
                                 show_sensors='upper right')
    plt.savefig(os.path.join(dir_meg_plots, 'erf-mag-gfp_UpVsDown.png'), format='png')
    mne.viz.plot_compare_evokeds([evoked_up, evoked_down], picks='grad',
                                 show_sensors='upper right')
    plt.savefig(os.path.join(dir_meg_plots, 'erf-grad-gfp_UpVsDown.png'), format='png')

    evokeds_diff_UpVsDown = mne.combine_evoked([evoked_up, evoked_down], weights=[1, -1])

    fig = evokeds_diff_UpVsDown.plot_joint(picks='mag')
    fig.set_size_inches((11, 7))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-mag_UpVsDown.png'), format='png')

    fig = evokeds_diff_UpVsDown.plot_joint(picks='grad')
    fig.set_size_inches((11, 7))
    plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-grad_UpVsDown.png'), format='png')
