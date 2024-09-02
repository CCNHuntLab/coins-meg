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

### Some initial settings

ifMaxfiltered = True

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
  - filter:             {l_freq: 0.25, h_freq: 100}
  - notch_filter:       {freqs: 50 100}
  - bad_segments:       {segment_len: 100, picks: mag, significance_level: 0.1}
  - bad_segments:       {segment_len: 100, picks: grad, significance_level: 0.1}
  - bad_segments:       {segment_len: 100, picks: mag, mode: diff, significance_level: 0.1}
  - bad_segments:       {segment_len: 100, picks: grad, mode: diff, significance_level: 0.1}
  - ica_raw:            {n_components: 64, picks: 'meg'}
  - ica_autoreject:     {picks: meg, ecgmethod: correlation, eogthreshold: auto}
  - interpolate_bads: {}
"""
# save config as yaml

config = yaml.safe_load(config_text)
with open('config.yaml', 'w') as file:
    yaml.dump(config, file)

# Read in the data ####
basedir = '/ohba/pi/lhunt/datasets/coins-meg_data/derivatives'
outdir = os.path.join(basedir, 'preprocessed', 'auto-max')

# make directory if it doesn't yet exist
os.makedirs(outdir, exist_ok=True)

# There are multiple runs for each subject. We will first fetch all data using an OSL utility
name = 'sub-{subj}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss'
fullpath = os.path.join(basedir, 'data_maxfiltered', 'sub-{subj}', name + '.fif')

print(fullpath)

datafiles = osl.utils.Study(fullpath)
print(datafiles)

# load all runs of all subjects
fnames = datafiles.get(subj="sub-19", run="run-4")
pprint(fnames)

# Create a text file with the path to each dataset on every line.
file = open('fnames.txt','w')
for item in fnames:
    file.write(item+"\n")
file.close()

#config = osl.preprocessing.load_config("config.yaml")# load in the config

# Apply the config to automate preprocessing ####
from osl.preprocessing import run_proc_batch

# process all subjects in parallel
run_proc_batch(config, fnames, outdir=outdir,
                   logsdir=os.path.join(outdir, 'logs'),
                   reportdir=os.path.join(outdir, 'report'),
                   overwrite=True)

#if __name__ == '__main__':
#    utils.logger.set_up(level="INFO")
#
#    from dask.distributed import Client
#    import glob
#    import osl
#    import numpy as np
#    import os
#    from multiprocessing import cpu_count
#
#    n_cores = multiprocessing.cpu_count()
#
#    client = Client(threads_per_worker=1, n_workers=6)
#
#    # write extra information here, e.g., definitions of config, files, output_dir
#
#    run_proc_batch(config, fnames, outdir=outdir,
 #                  logsdir=os.path.join(outdir, 'logs'),
 #                  reportdir=os.path.join(outdir, 'report'),
 #                  overwrite=True,
 #                  dask_client=True)

'''