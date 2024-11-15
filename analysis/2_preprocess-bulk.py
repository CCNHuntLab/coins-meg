# We will make a config dictionary that contains all preprocessing steps in one place,
# and then apply all steps in sequence using a single function call to OSL

import os
import osl
import mne
from pprint import pprint
import yaml
import ipympl
from osl import preprocessing, utils
import coinsmeg_data as coinsmeg
from dask.distributed import Client, as_completed # for parallel processing
import sys

### The preprocessing config ####

config_text= """
meta:
  event_codes:
    laserHit: 1
    laserMiss: 2
    keyRight: 3
    keyLeft: 4
    keyUp: 5
    keyDown: 6
    keyRelease: 7
    blockStart: 10
    blockEnd: 20
    expStart: 100
    expEnd: 105
preproc:                                   
  - find_events:        {min_duration: 0.005}
  - set_channel_types:  {EOG001: eog, EOG002: eog, ECG003: ecg}
  - filter:             {l_freq: 0.25, h_freq: 40, method: iir, iir_params: {order: 5, ftype: butter}}
  - notch_filter:       {freqs: 50 100}
  - resample: {sfreq: 250}
  - bad_segments: {segment_len: 250, picks: mag}
  - bad_segments: {segment_len: 250, picks: grad}
  - bad_segments: {segment_len: 250, picks: mag, mode: diff}
  - bad_segments: {segment_len: 250, picks: grad, mode: diff}
  - bad_channels: {picks: mag}
  - bad_channels: {picks: grad}
  - ica_raw: {picks: meg, n_components: 64}
  - ica_autoreject:     {picks: meg, ecgmethod: correlation, eogthreshold: auto}
  - interpolate_bads: {}
"""
# save config as yaml

config = yaml.safe_load(config_text)
with open('config.yaml', 'w') as file:
    yaml.dump(config, file)

# Read in the data ####
basedir = coinsmeg.DERIVATIVES_DIR 
outdir = coinsmeg.PREPROCESSED_DIR 
print(outdir)

# make directory if it doesn't yet exist
os.makedirs(outdir, exist_ok=True)

# There are multiple runs for each subject. We will first fetch all data using an OSL utility
name = 'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss'
fullpath = os.path.join(coinsmeg.DERIVATIVES_DIR, 'maxfiltered', 'sub-{subj}', name + '.fif')

print(fullpath)

datafiles = osl.utils.Study(fullpath)
print(datafiles)

# load all runs of all subjects
fnames = datafiles.get()
#names = datafiles.get(subj="17", run="1") # load a test subject/run
#pprint(fnames)
print(fnames)

# Create a text file with the path to each dataset on every line.
file = open('fnames.txt','w')
for item in fnames:
    file.write(item+"\n")
file.close()

config = osl.preprocessing.load_config("config.yaml")# load in the config

# Apply the config to automate preprocessing ####

# process all subjects in parallel
# Parallelize processing using Dask
def preprocess_subject(fname):
    """Function to preprocess a single dataset."""
    preprocessing.run_proc_batch(
        config,
        [fname],  # single filename to be processed by each worker
        outdir=outdir,
        logsdir=os.path.join(outdir, 'logs'),
        reportdir=os.path.join(outdir, 'report'),
        overwrite=True
    )

if __name__ == "__main__":
    utils.logger.set_up(level="INFO")

    # Set up Dask client for parallel processing
    client = Client(n_workers=4, threads_per_worker=1)

    # Submit tasks for each file to the Dask client
    futures = [client.submit(preprocess_subject, fname) for fname in fnames]

    # Collect and wait for all tasks to complete
    for future in as_completed(futures):
        try:
            result = future.result()
            print(f"Completed processing for: {result}")
        except Exception as e:
            print(f"Processing failed with error: {e}")

    client.close()


