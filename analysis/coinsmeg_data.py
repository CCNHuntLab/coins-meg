"""
Utilities to construct file paths and load data from the COINS-MEG dataset.
"""

import os.path as op

#
# Constants defining directory names, file names, and other path components.
#

# Base directory within which all the data of the COINS-MEG dataset is stored.
BASE_DIR = "/ohba/pi/lhunt/datasets/coins-meg_data"

# Raw data are stored directly in the base directory.
RAW_DIR = BASE_DIR

# Subdirectory containing the behavioral and MEG data for the MEG session,
# located within each of the subject-specific, raw data directories.
MEG_SESS_SUBDIR = "ses-2-meg"

# Subdirectory containing the behavioral data for the MEG session.
BEHAV_SUBDIR = op.join(MEG_SESS_SUBDIR, "beh")

# Subdirectory containing the MEG data for the MEG session.
MEG_SUBDIR = op.join(MEG_SESS_SUBDIR, "meg")

# Subdirectory containing the anatomical MRI data, located within the each of the
# subject-specific, raw data directories.
ANAT_SUBDIR = "ses-3-structural/anat"

# Derivatives directory, containing preprocessed data as well as all other data
# that was derived from the raw data.
DERIVATIVES_DIR = op.join(BASE_DIR, "derivatives")

# Directory containing preprocessed data.
PREPROCESSED_DIR = op.join(DERIVATIVES_DIR, "preprocessed")

# Directory containing source-space parcellated data
SRC_DIR = op.join(DERIVATIVES_DIR, "src")

#
# Definitions of events, conditions, and other experiment-related information.
#

EVENT_ID = {
    "blockEnd": 20,
    "blockStart": 10,
    "expEnd": 105,
    "expStart": 100,
    "keyDown": 6,
    "keyLeft": 4,
    "keyRelease": 7,
    "keyRight": 3,
    "keyUp": 5,
    "laserHit": 1,
    "laserMiss": 2,
}

#
# Definitions related to the subjects in the dataset.
#

def sub_num2str(sub_num):
    """
    Convert a subject number to a string of the form 'sub-XX',
    which is the way subjects are identified in the dataset file structure.
    """
    return f'sub-{sub_num:02d}'

# List of all subjects in the dataset.
SUB_NUMS_ALL = list(range(1, 23))
SUBS_ALL = [sub_num2str(subnum) for subnum in SUB_NUMS_ALL]

# List of subjects with anatomical data (structural MRI), as documented
# in docs/coinsmeg_participant_notes/if-data-in-directory.xlsx in this repository.
SUB_NUMS_W_ANAT = [4, 7] + list(range(9, 22))
SUBS_W_ANAT = [sub_num2str(subnum) for subnum in SUB_NUMS_W_ANAT]

# Number of runs in the MEG session, and list of run numbers identifying each run.
N_RUNS = 4
RUNS = list(range(1, N_RUNS+1))

#
# Subject-specific directories and file paths
#

def get_sub_dir(parent_dir, sub):
    """
    Path to the directory for a given subject within a parent directory.
    E.g., get_sub_dir(RAW_DIR, 'sub-07') returns the directory containing the raw
    data for subject 7.
    """
    return op.join(parent_dir, sub)

def get_sub_behav_dir(sub):
    """Path to the directory containing the behavioral data (MEG session)
    for a given subject."""
    return op.join(get_sub_dir(RAW_DIR, sub), BEHAV_SUBDIR)

def get_sub_meg_dir(sub):
    """Path to the directory containing the MEG data for a given subject."""
    return op.join(get_sub_dir(RAW_DIR, sub), MEG_SUBDIR)

def get_sub_anat_dir(sub):
    """Path to the directory containing the anatomical MRI for a given subject."""
    return op.join(get_sub_dir(RAW_DIR, sub), ANAT_SUBDIR)

def get_sub_behav_fname(sub, runnum):
    """Name of the file containing the behavioral data for a given subject and
    run number."""
    return f'{sub}_ses-2-meg_task-coinsmeg_run-{runnum}.csv'

def get_sub_behav_fpath(sub, runnum):
    """Path to the file containing the behavioral data for a given subject and
    run number."""
    d = get_sub_behav_dir(sub)
    fname = get_sub_behav_fname(sub, runnum)
    return op.join(d, fname)

def get_sub_preproc_dir(sub, run):
    """Path to the directory containing the preprocessed MEG data for a given subject
    and run."""
    subdir = f"{sub_num2str(sub)}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss"
    return op.join(PREPROCESSED_DIR, subdir)

def get_sub_preproc_raw_fname(sub, run):
    """Name of the .fif file containing the preprocessed MEG data for a given
    subject and run, which can be loaded as a MNE Raw object."""
    return f"{sub_num2str(sub)}_ses-2-meg_task-coinsmeg_run-{run}_meg_transsss_preproc_raw.fif"

def get_sub_preproc_raw_fpath(sub, run):
    """Path to the .fif file containing the preprocessed MEG data for a given
    subject and run, which can be loaded as a MNE Raw object."""
    d = get_sub_preproc_dir(sub, run)
    fname = get_sub_preproc_raw_fname(sub, run)
    return op.join(d, fname)

def get_sub_src_dir(sub, run):
    """Path to the directory containing the source-reconstructed MEG data
    for a given subject and run."""
    return op.join(SRC_DIR, f"{sub_num2str(sub)}_run-{run}")

def get_sub_src_parc_fpath(sub, run):
    """Path to the .fif file containing the source-reconstructed MEG data
    for a given subject and run, parcellated by brain region, and
    loadable as a MNE Raw object."""
    d = get_sub_src_dir(sub, run)
    fname = "parc_raw.fif"
    return op.join(d, fname)
