# ------------------------ Script for maxfiltering prior to preprocessing ------------------------ ####

# created axl 18/9/23
# adapted from oliver kohl

# This script first identifies the most central run/scan for each participant.
# Participants did 4 runs * 4 blocks of the COINS task; note that each run was a separate scan/.fif file.
# For each participant, we identify the most central of the 4 runs, so that we can align the head position
# of the other runs from that participant to the most central run when applying maxfilter.

# Import packages ####
import mne
import os
import math
import collections
import numpy as np
from glob import glob
from scipy import linalg
from osl.maxfilter import run_maxfilter_batch
import coinsmeg_data as coinsmeg
import sys

# Define functions ####
# distance between two points in 3D-coordinate system
def dist(point_1, point_2, key):
    x = math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1]- point_2[1])**2 + (point_1[2]- point_2[2])**2)
    return(x)

# Read in the data ####

excludes = [] # participants to exclude; currently none

raw_path = coinsmeg.BASE_DIR
#raw_path = "/Users/amyli/Desktop/LH-lab/coins-meg_meg-analysis/data"
raw_folder = [name for name in glob(raw_path + "/*/ses-2-meg/meg/")]
raw_folder = [folder for folder in raw_folder if folder.split('/')[-4] not in excludes] # get rid of folders of subs to exclude
raw_folder = sorted(raw_folder)

# make list of subjects
subjs = {file.split("/")[-1] for file in glob(raw_path + "/sub-*")} # ensure that only folders beginning with "sub-" are included in subjs
subjs = [sub for sub in subjs if sub not in excludes] # drop subjects who did not complete task
subjs = dict.fromkeys(subjs) #create dictionary with empty value
subjs = collections.OrderedDict(sorted(subjs.items())) #sort dictionary by key

# example in comments: only do subject 19
#subjs = collections.OrderedDict([list(subjs.items())[18]]) 
## need to convert back to OrderedDict, else "subjs.keys()" in the below for loop will not work
#raw_folder = [raw_folder[18]] # only do subject 19 now
print("subjs = ",subjs)

# %% Identify most central scan for each participant ####

# this will break if a subject (folder sub-XX) has a "meg" folder (i.e., their directory is listed in raw_folder)
# but there is no actual data in it
# however, it CAN deal with a subject having a sub-XX folder that doesn't contain a "meg" subfolder

runs_all = []
for i, folder in enumerate(sorted(raw_folder)):  # for each subject (aka each subject folder)

    raw_dict = {}
    origin_dict = {}
    dev_origin_dict = {}

    runs = sorted(os.listdir(folder))  # blocks: all files in one subject folder
    runs = [block for block in runs if block.endswith('.fif')]  # Make sure to only keep .fif files

    print(folder, runs)

    for j, files in enumerate(runs):
        raw_dict[runs[j]] = mne.io.read_raw_fif(folder + files, allow_maxshield=True, preload=False)
        matrix = linalg.inv(raw_dict[runs[j]].info['dev_head_t']['trans'])  # inverse transform into head->dev
        origin_dict[runs[j]] = matrix[:3, 3]  # get origin coordinates for each block and save in dictionary

    mean_origin = sum(origin_dict.values()) / len(runs)  # get mean origin-coordinates across all blocks
    distance_dict = {key: dist(origin_dict[key], mean_origin, key) for key in
                     origin_dict}  # get distance between coordinates of mean and origin-coordinates for each block
    central_scan = min(distance_dict,
                       key=distance_dict.get)  # get most central scan (i.e., scan that is closest to mean)

    subjs[list(subjs.keys())[i]] = central_scan  # save most central scan in dictionary
    runs_all.append(runs)

# central_scan = [central_scan] # necessary if testing a single run/file

# Print results
most_central = subjs
for i, subject in most_central.items():  # go through each subject folder
    print("Most central scan for subject " + str(i) + ": " + str(subject))

# Run maxfilter ####

# Loop Through participants and Maxfilter files while aligning to the most central run

for iSub, central_scan in enumerate(most_central.items()):
    # when you use enumerate(most_central.items()), you'll get an iterator that yields tuples containing both the index and a key-value pair from your dictionary.
    # e.g., [(0, ('sub-12', 'sub-12_ses-2-meg_task-coinsmeg_run-3_meg.fif'))]
    # would have iSub = 0, central_scan will be the tuple ('sub-12', 'sub-12_ses-2-meg_task-coinsmeg_run-3_meg.fif')

    # Set Folder and Blocks with Data for participant
    folder = raw_folder[iSub]
    runs = runs_all[iSub]

    # Set Path to maxfilter input files or participant
    input_files = [folder + run for run in runs]

    # Set Path to most central block
    trans_file = folder + central_scan[1] # recall that central_scan will be  eg the tuple ('sub-12', 'sub-12_ses-2-meg_task-coinsmeg_run-3_meg.fif')
    # so central_scan[1] is the filename of the most central scan

    # Directory to save the maxfiltered data to
    output_dir = f"{coinsmeg.DERIVATIVES_DIR}/maxfiltered/" + central_scan[0] + '/'
    print('output_dir = ',output_dir)
 
    # Run MaxFiltering
    run_maxfilter_batch(
        input_files,
        output_dir,
        f"--maxpath /neuro/bin/util/maxfilter --mode multistage --scanner Neo --tsss --headpos --movecomp --trans {trans_file}",)
        #  the maxfilter aligns all runs of a participant so that the head position is the same within each participant
