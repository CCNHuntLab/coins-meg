## Some first analyses (e.g., ERFs) ####
from matplotlib import pyplot as plt
import mne
import osl
import numpy as np
import os
import pandas as pd
from mne.preprocessing import create_eog_epochs

# Read in the data ####
basedir = '/Users/amyli/Desktop/LH-lab/coins-meg_meg-analysis/'
#basedir = '/ohba/pi/lhunt/datasets/coins-meg_meg-analysis'
subj = 12
run = 2
ifMaxfiltered = False

procdir = os.path.join(basedir, 'preprocessed', f'sub-{subj}', f'run-{run}')
#procdir = os.path.join(basedir, 'preprocessed')

if ifMaxfiltered == False:
    #dir_meg = os.path.join(procdir, 'auto-nomax', f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg') # for output from run_proc_chain
    dir_meg = os.path.join(procdir, 'meg', 'nomax')
else:
    dir_meg = os.path.join(procdir, 'meg', 'max')  # folder where maxfiltered versions live

dir_meg_derivatives = os.path.join(dir_meg, 'derivatives') # for storing derivatives from processing (eg fif files)
dir_meg_plots = os.path.join(dir_meg, 'plots') # for storing plots generated during preprocessing

# generate the output directory if it doesn't exist
os.makedirs(dir_meg_derivatives, exist_ok=True)
os.makedirs(dir_meg_plots, exist_ok=True)

## Read in the MEG data

# Get the filename for a specific subject and run
if ifMaxfiltered == False:
    #preproc_fname = os.path.join(dir_meg, f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_preproc_raw.fif')
    preproc_fname = os.path.join(dir_meg_derivatives,
                                 f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_preproc_raw.fif')
else:
    preproc_fname = os.path.join(dir_meg_derivatives,
                                 f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss_preproc_raw.fif')

clean = mne.io.read_raw_fif(preproc_fname, preload=True)

# Define the events
events = mne.find_events(clean, min_duration=0.005)
event_color = {}
event_dict = {'laserHit': 1, 'laserMiss': 2, 'keyRight': 3, 'keyLeft': 4, 'keyUp': 5, 'keyDown': 6, 'keyRelease': 7}

# Create epochs for hits and misses

epochs = mne.Epochs(clean, events, tmin=-0.5, tmax=1.0, event_id=event_dict) # -0.5-1.0
print(epochs)

print(f"epochs has the following size [epoch x channel x time]: {epochs.get_data().shape}")

# Remove epochs with particularly high peak-to-peak amplitudes, as this indicates there might still
# # be segments in the data with high variance, that we didn't find earlier. We also include EOG peak-to-peak
# amplitude, as high amplitudes indicate saccades.
epochs.drop_bad({"eog": 6e-4, "mag": 4e-11, "grad": 4e-10}) # defines specific thresholds for peak-to-peak amplitudes in different types of channels
# diff sensor types have diff units

epochs.plot_drop_log()
plt.savefig(os.path.join(dir_meg_plots, 'epoch-drop_-0.5-1.0.png'), format='png')

# use equalize_event_counts first to randomly sample epochs from each condition to match the number
# of epochs present in the condition w/ the fewest good epochs
conditions = ["laserHit", "laserMiss"]
epochs.equalize_event_counts(conditions)

hit_epochs = epochs["laserHit"]
miss_epochs = epochs["laserMiss"]

# Check channel locations/names
mne.viz.plot_sensors(clean.info, kind='3d')

#hit_epochs.plot_image(picks=["MEG1831"], title="MEG1831, laserHit")
#plt.savefig(os.path.join(dir_meg_plots, 'erf_laserHit.png'), format='png')

#miss_epochs.plot_image(picks=["MEG1831"], title="MEG1831, laserMiss")
#plt.savefig(os.path.join(dir_meg_plots, 'erf_laserMiss.png'), format='png')

# Compute average evoked responses for hit and miss epochs

## hit ERFs
evoked_hit = hit_epochs.average()

evoked_hit.plot_joint(picks='mag')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_laserHit.png'), format='png')

evoked_hit.plot_joint(picks='grad')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_laserHit.png'), format='png')

### centroparietal only
roi_cp = ['MEG0731', 'MEG0741', 'MEG1831', 'MEG2241'] # define roi over centroparietal sensors

evoked_hit.plot_joint(picks=roi_cp)
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag-cp_laserHit.png'), format='png')

## miss ERFs
evoked_miss = miss_epochs.average()

evoked_miss.plot_joint(picks='mag')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_laserMiss.png'), format='png')

evoked_miss.plot_joint(picks='grad')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_laserMiss.png'), format='png')

### centroparietal only
evoked_miss.plot_joint(picks=roi_cp)
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag-cp_laserMiss.png'), format='png')

## Compare hit vs miss evokeds

mne.viz.plot_compare_evokeds([evoked_hit, evoked_miss], picks='mag',
                             show_sensors='upper right')
plt.savefig(os.path.join(dir_meg_plots, 'erf-mag-gfp_hitVsMiss.png'), format='png')

## difference waveform hit-miss

### all sensors and topography
evokeds_diff_hitVsMiss = mne.combine_evoked([evoked_hit, evoked_miss], weights=[1, -1])
evokeds_diff_hitVsMiss.plot_joint(picks='mag')
plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-mag_hitVsMiss.png'), format='png')
evokeds_diff_hitVsMiss.plot_joint(picks='grad')
plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-grad_hitVsMiss.png'), format='png')

### cp sensors
mne.viz.plot_compare_evokeds({'Hit-Miss':evokeds_diff_hitVsMiss},
                             picks=roi_cp, show_sensors='upper right',
                             combine='mean',
                             title='Difference Wave')

plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-mag-cp_hitVsMiss.png'), format='png')

plt.show()

# Create epochs for movement keys (left vs right)

epochs = mne.Epochs(clean, events, tmin=-3.0, tmax=1.0, event_id=event_dict) # different epoch times now compared to hit/miss
print(epochs)

# Remove epochs with particularly high peak-to-peak amplitudes, as we did for hit/miss epochs

epochs.drop_bad({"eog": 6e-4, "mag": 4e-11, "grad": 4e-10}) # defines specific thresholds for peak-to-peak amplitudes in different types of channels
epochs.plot_drop_log()

# use equalize_event_counts first to randomly sample epochs from each condition to match the number
# of epochs present in the condition w/ the fewest good epochs
conditions = ["keyLeft", "keyRight"]
epochs.equalize_event_counts(conditions)

left_epochs = epochs["keyLeft"]
right_epochs = epochs["keyRight"]

# Plot ERF for just a single channel
left_epochs.plot_image(picks=["MEG1831"], title="MEG1831, keyLeft")
plt.savefig(os.path.join(dir_meg_plots, 'erf_keyLeft.png'), format='png')

right_epochs.plot_image(picks=["MEG1831"], title="MEG1831, keyRight")
plt.savefig(os.path.join(dir_meg_plots, 'erf_keyRight.png'), format='png')

# Compute average evoked responses for left and right epochs

evoked_left = left_epochs.average()
evoked_left.plot_joint(picks='mag')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_keyLeft.png'), format='png')
evoked_left.plot_joint(picks='grad')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_keyLeft.png'), format='png')

evoked_left.plot_joint(picks=roi_cp)
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag-cp_keyLeft.png'), format='png')

evoked_right = right_epochs.average()
evoked_right.plot_joint(picks='mag')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag_keyRight.png'), format='png')
evoked_right.plot_joint(picks='grad')
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-grad_keyRight.png'), format='png')

evoked_right.plot_joint(picks=roi_cp)
plt.savefig(os.path.join(dir_meg_plots, 'erf-joint-mag-cp_keyRight.png'), format='png')


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
evokeds_diff_leftVsRight.plot_joint(picks='mag')
plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-mag_leftVsRight.png'), format='png')
evokeds_diff_leftVsRight.plot_joint(picks='grad')
plt.savefig(os.path.join(dir_meg_plots, 'erf-diff-joint-grad_leftVsRight.png'), format='png')