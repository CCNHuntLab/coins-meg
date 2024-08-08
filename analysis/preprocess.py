# Import packages ####

from matplotlib import pyplot as plt

import mne
import osl
import numpy as np
import os
#import ipympl

from pprint import pprint
import glob
import pandas as pd
from mne.preprocessing import create_eog_epochs

# Read in the data ####
basedir = '/Users/amyli/Desktop/LH-lab/coins-meg_meg-analysis/'
#basedir = '/ohba/pi/lhunt/datasets/coins-meg_meg-analysis'
subj = 12 # this isn't really being used at the moment except to specify ICA output file
run = 1
ifMaxfiltered = True

outdir = os.path.join(basedir, 'preprocessed', f'sub-{subj}', f'run-{run}')

if ifMaxfiltered == False:
    outdir_meg = os.path.join(outdir, 'meg', 'nomax')  # for any meg-related outputs
else:
    outdir_meg = os.path.join(outdir, 'meg', 'max') # for any meg-related outputs

outdir_meg_plots = os.path.join(outdir_meg, 'plots') # for storing plots generated during preprocessing
outdir_meg_derivatives = os.path.join(outdir_meg, 'derivatives') # for storing derivatives from processing (eg fif files)

# generate the output directory if it doesn't exist
os.makedirs(outdir, exist_ok=True)
os.makedirs(outdir_meg, exist_ok=True)
os.makedirs(outdir_meg_plots, exist_ok=True)
os.makedirs(outdir_meg_derivatives, exist_ok=True)

## Read in the MEG data

# Get the filename for a specific subject and run

if ifMaxfiltered == False:
    name = f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg'
    fullpath = os.path.join(basedir, 'data', f'sub-{subj}', 'ses-2-meg', 'meg', name + '.fif')
else:
    name = f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss'
    fullpath = os.path.join(basedir, 'data_maxfiltered', f'sub-{subj}', name + '.fif')

raw = mne.io.read_raw_fif(fullpath, preload=True)

## Read in the behavioural data outputted by psychopy
name_beh = f'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}'
fullpath_beh = os.path.join(basedir, 'data', f'sub-{subj}', 'ses-2-meg', 'beh', name_beh + '.csv')
print(fullpath_beh)

raw_beh = pd.read_csv(fullpath_beh)
print(raw_beh.to_string())

# Inspect the data ####

print(raw.info) # a python dictionary
print('data dimensions are: ', raw.get_data().shape)  # data dimensions (channels by time)

# print the channel names
print(raw.ch_names)

## Inspect events ####

####    trigger list:
# expStart      = 100;
# practiceMove  = 101;
# practiceSize  = 102;
# expEnd        = 105;
# lastFrame     = 99;
#
# blockStart    = 10;
# blockEnd      = 20;
#
# laserHit      = 1;
# laserMiss     = 2;
#
# keyRight      = 3;
# keyLeft       = 4;
# keyUp         = 5;
# keyDown       = 6;
# keyRelease    = 7;

events = mne.find_events(raw, min_duration=0.005)
event_color = {}
event_dict = {'laserHit': 1, 'laserMiss': 2, 'keyRight': 3, 'keyLeft': 4, 'keyUp': 5, 'keyDown': 6, 'keyRelease': 7, 'blockStart': 10, 'blockEnd': 20}

# Plot events
fig, ax = plt.subplots(1,1, figsize=(8,6))
fig = mne.viz.plot_events(events, sfreq=raw.info['sfreq'], event_id=event_dict, on_missing='ignore', verbose='error', axes=ax, show=True)

# Save the plot
fig_outpath = os.path.join(outdir_meg_plots, 'triggers-meg.png')
plt.savefig(fig_outpath)

# Compare the events to the ones inside psychopy-generated csv file

# add a time column; assume screen refresh rate of 100Hz
raw_beh['expTime'] = range(0, 43196 * 10, 10) # 100Hz = 1 new frame every 10ms

# Create a list of unique trigger values
unique_triggers = sorted(set(event_dict.values()))
colors = plt.cm.viridis(np.linspace(0, 1, len(unique_triggers)))

# Create a figure and axes for the plot
fig, ax = plt.subplots(figsize=(10, 6))
# Initialize a dictionary to store the count of each trigger
trigger_counts = {key: 0 for key in event_dict.keys()}

# Loop through unique triggers and plot each as a separate row
for idx, trigger_value in enumerate(unique_triggers):
    # Filter the DataFrame for rows with the current trigger value
    filtered_data = raw_beh[raw_beh[" 'triggerValue'"] == trigger_value]

    # Get the trigger label for the current trigger value
    trigger_label = list(event_dict.keys())[list(event_dict.values()).index(trigger_value)]

    # Count the occurrences of the current trigger
    trigger_count = len(filtered_data)

    # Update the trigger_counts dictionary
    trigger_counts[trigger_label] = trigger_count

    # Plot expTime vs. trigger_value for the current trigger, with label
    ax.scatter(filtered_data['expTime'], [idx] * len(filtered_data), label=f'{trigger_label} ({trigger_count})',
               color=colors[idx])

# Set y-axis labels based on trigger labels
ax.set_yticks(range(len(unique_triggers)))
ax.set_yticklabels(list(event_dict.keys()))

# Add labels and legend
ax.set_xlabel('expTime')
ax.set_ylabel('Trigger Type')
ax.set_title('Trigger Occurrence Over Time')
# Create a legend with custom labels
legend_labels = [f'{key} ({trigger_counts[key]})' for key in event_dict.keys()]
ax.legend(labels=legend_labels)

# Save the plot
fig_outpath = os.path.join(outdir_meg_plots, 'triggers-psychopy.png')
plt.savefig(fig_outpath)

## Inspect the raw data ####
raw.set_channel_types({"EOG001": "eog", "EOG002": "eog", "ECG003": "ecg"})  # set the eog and ecg channels
raw.plot(n_channels=20)  # plot 20 channels

# Check data quality: 1) variance of the data (over time, and over channels)...

## Let's create a function with which we can easily look at the variance of the data
def plot_var(raw):
    mag = raw.get_data(picks='mag', reject_by_annotation='NaN')
    grad = raw.get_data(picks='grad', reject_by_annotation='NaN')

    fig, ax = plt.subplots(2,2)
    plt.axes(ax[0,0])
    plt.plot(raw.times, np.nanvar(grad, axis=0)), plt.title('GRAD'),  plt.xlabel('Time (s)'), plt.ylabel('Variance')
    plt.axes(ax[1,0])
    plt.plot(raw.times, np.nanvar(mag, axis=0)), plt.title('MAG'), plt.xlabel('Time (s)'), plt.ylabel('Variance')

    plt.axes(ax[0,1])
    plt.hist(np.nanvar(grad, axis=1), bins=24, histtype='step'), plt.title('GRAD'), plt.xlabel('Variance')
    plt.axes(ax[1,1])
    plt.hist(np.nanvar(mag, axis=1), bins=24, histtype='step'), plt.title('MAG'), plt.xlabel('Variance')

    plt.tight_layout()
    plt.show()
    return fig, ax

## Now plot variance over time and over channels - seperately for each channel type
fig, ax = plot_var(raw)
plt.savefig(os.path.join(outdir_meg_plots, 'var_raw.png'), format='png')

# ... and the frequency domain power spectral density (PSD, or power spectrum)
psd = raw.compute_psd(picks='meg')
fig, ax = plt.subplots(2,1, figsize = (8,6))
fig = psd.plot(axes=ax)
plt.suptitle('Note the peaks at 50 Hz and 100 Hz in the plots - this corresponds to line noise')

# Save the plot
plt.savefig(os.path.join(outdir_meg_plots, 'psd_raw.png'), format='png')

## Preprocess the data ####

### Bandpass between 0.25 and 100Hz ####
psd = raw.compute_psd(picks='meg')
fig, ax = plt.subplots(2,2, figsize = (8,6))
psd.plot(axes=ax[:,0])
ax[0,0].set_title('Raw data \n Gradiometers (204 channels)')

raw_bp = raw.copy().filter(l_freq=0.25, h_freq=100) # suggested to set l_freq to 1.0 for ICA
psd_bp = raw_bp.compute_psd(picks='meg')

### Notch filter at 50 and 100 Hz ####

# Now use a notch filter and plot again. (Note that we first copy the raw data so that we keep an original copy).
freqs = (50, 100) # where peaks are indicative of line noise
raw_notch = raw_bp.copy().notch_filter(freqs=freqs, picks='meg')
psd_notch = raw_notch.compute_psd(picks='meg')

# plot the previous two figures again
fig, ax = plt.subplots(2,3, figsize = (10,6))
psd.plot(axes=ax[:,0])
ax[0,0].set_title('Raw data \n Gradiometers')
psd_bp.plot(axes=ax[:,1])
ax[0,1].set_title('After band-pass (BP) filter \n Gradiometers')

# plot the BP + notch filtered PSD
psd_notch.plot(axes=ax[:,2]) # See the plot above
ax[0,2].set_title('After BP and notch filter \n Gradiometers')

# Make sure the y-axes are the same, to ease comparison
[ax[0,i].set_ylim((0,30)) for i in range(3)]
[ax[1,i].set_ylim((0,70)) for i in range(3)]

# Save the plot
plt.savefig(os.path.join(outdir_meg_plots, 'psd_bp-notch.png'), format='png')

### Bad segment/channel detection - do separately for each channel type

# Bad segment detection
raw_badseg = osl.preprocessing.osl_wrappers.detect_badsegments(raw_notch.copy(), picks='grad', segment_len=1000)
raw_badseg = osl.preprocessing.osl_wrappers.detect_badsegments(raw_badseg, picks='mag')
fig, ax = plot_var(raw_badseg)

# Save the plot
plt.savefig(os.path.join(outdir_meg_plots, 'var_bp-notch-badseg.png'), format='png')

# Bad channel detection
raw_badchan = osl.preprocessing.osl_wrappers.detect_badchannels(raw_badseg.copy(), picks='grad')
raw_badchan = osl.preprocessing.osl_wrappers.detect_badchannels(raw_badchan, picks='mag')
print(f"These channels were marked as bad: {raw.info['bads']}")

## Visualise again
fig, ax = plot_var(raw_badchan)
plt.savefig(os.path.join(outdir_meg_plots, 'var_bp-notch-badseg-badchan.png'), format='png')

## See raw data - notice how bad segments are marked
raw_badchan.plot(duration=100, n_channels=50)

## Do the ICA
ica = mne.preprocessing.ICA(n_components=64, random_state=42) # check which grad/mag it's doing ica on
ica.fit(raw_badchan.copy().filter(l_freq=1, h_freq=None))

ica.save(os.path.join(outdir_meg_derivatives, 'ica_bp-notch-badseg-badchan.fif'), overwrite=True)

## Visualise EOG and ECG artifacts

from mne.preprocessing import ICA, corrmap, create_ecg_epochs, create_eog_epochs

# We can get a summary of how the ocular artifact manifests across each channel type using create_eog_epochs
eog_evoked = create_eog_epochs(raw_badchan).average()
eog_evoked.apply_baseline(baseline=(None, -0.2))

eog_evoked.plot_joint(picks='mag')
plt.savefig(os.path.join(outdir_meg_plots, 'eog-mag_bp-notch-badseg-badchan.png'), format='png')

eog_evoked.plot_joint(picks='grad')
plt.savefig(os.path.join(outdir_meg_plots, 'eog_grad-bp-notch-badseg-badchan.png'), format='png')

# Now we’ll do the same for the heartbeat artifacts, using create_ecg_epochs:
ecg_evoked = create_ecg_epochs(raw_badchan).average()
ecg_evoked.apply_baseline(baseline=(None, -0.2))

ecg_evoked.plot_joint(picks='mag')
plt.savefig(os.path.join(outdir_meg_plots, 'ecg-mag_bp-notch-badseg-badchan.png'), format='png')

ecg_evoked.plot_joint(picks='grad')
plt.savefig(os.path.join(outdir_meg_plots, 'ecg-grad_bp-notch-badseg-badchan.png'), format='png')

## Use ECG and EOG data to correct artifacts in the data

# Find which ICs match the ECG pattern

# EEG063 corresponds to the ECG
ecg_indices, ecg_scores = ica.find_bads_ecg(raw_badchan, ch_name='ECG003', method='correlation', threshold='auto')
#ecg_indices, ecg_scores = ica.find_bads_ecg(raw, ch_name='ECG003', method='ctps', threshold='auto')

# check what ctps is doing (at least vaguely)
# returns the normalized Kuiper index scores
# Note we use cross-trial phase statistics (method='ctps') rather than correlation here.
# Threshold is decided on by the _get_ctps_threshold function,
#         Automatically decide the threshold of Kuiper index for CTPS method.
#         This function finds the threshold of Kuiper index based on the
#         threshold of pk. Kuiper statistic that minimizes the difference between
#         pk and the pk threshold (defaults to 20) is returned. It is assumed that the data
#         are appropriately filtered and bad data are rejected at least based on peak-to-peak amplitude
#         when/before running the ICA decomposition on data.

# save figures for time courses of ics that are identified as correlated w/ EOG & ECG

ica.plot_components(ecg_indices) # will return error if nothing in ecg_indices
plt.savefig(os.path.join(outdir_meg_plots, 'ecg-ics_bp-notch-badseg-badchan.png'), format='png')

ica.plot_sources(raw, picks=ecg_indices)

# barplot of ICA component "ECG match" scores
ica.plot_scores(ecg_scores)
# save this figure
plt.savefig(os.path.join(outdir_meg_plots, 'ecg-ics-scores_bp-notch-badseg-badchan.png'), format='png')

# Find which ICs match the EOG pattern

# EOG001 corresponds to horizontal EOG (HEOG), EOG002 to vertical EOG (VEOG)
eog_indices, eog_scores = ica.find_bads_eog(raw_badchan, ch_name=['EOG001', 'EOG002'])
#   Detection is based on Pearson correlation between the filtered data and the filtered EOG channel.
#   Thresholding is based on adaptive z-scoring. The above threshold
#   components will be masked and the z-score will be recomputed
#   until no supra-threshold component remains.

ica.plot_components(eog_indices) # visualise the components
plt.savefig(os.path.join(outdir_meg_plots, 'eog-ics_bp-notch-badseg-badchan.png'), format='png')

# barplot of ICA component "EOG match" scores
ica.plot_scores(eog_scores)
# save this figure
plt.savefig(os.path.join(outdir_meg_plots, 'eog-ics-scores_bp-notch-badseg-badchan.png'), format='png')

# Remove bad components from the data

ica.exclude = list(np.unique(eog_indices + ecg_indices)) # concatenate the two lists of components,
# and save unique components to ica.exclude which is then used by ica.apply to exclude the components
clean = ica.apply(raw_badchan.copy())

# save the clean data
preproc_fname = os.path.join(outdir_meg_derivatives, fullpath.rsplit('/', 1)[-1].replace('.fif', '_preproc_raw.fif'))
print(preproc_fname)
clean.save(preproc_fname, overwrite=True)