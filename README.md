## coins-meg_meg-analysis README

##### Last updated AXL 08/08/2023

COINS-MEG analysis repo.

### Folder Structure

See `.gitignore` for more details of which files are ignored in commits.

Scripts in the repo should write to `/ohba/pi/lhunt/datasets/coins-meg_meg-analysis/derivatives`.

- `analysis` contains:

  - `preprocess-maxfilter.py` which maxfilters the data.
  - `preprocess-bulk.py` which bulk-preprocesses multiple runs/multiple subjects using osl's batch preprocess tool
    - osl batch preprocess function also outputs the `config.yaml` (preprocess settings) and `fnames.txt` (paths of all files to be preprocessed).
  - `preprocess.py` - can ignore; an earlier manual version of the preprocessing script, which implements each preprocessing step with MNE Python.
  - `bulkprepro-prelim-analysis.ipynb` - preliminary data visualisation and ERF plotting
    - `bulkprepro-prelim-analysis_bulk.py` - does the same thing, but bulk-runs it for specificed participants/runs, and suppresses plot pop-ups while saving them inside `preprocessed/sub-{subj}/run-{run}/meg/auto-max/plots`
  - `glm-prelim.ipynb` does some _very_ preliminary experimenting with GLM-spectrum.
  - A virtual environment folder `venv` which should be ignored as it will not work across computers.
- `data` stores the following:

  - BIDS-formatted data - each subject (`sub-XX`) has the following subfolders:
    - `ses-1-training`: data from the laptop-based training prior to going into the MEG scanner. Contains two runs in two separate csv files. `run-1` contains 2 easy and 2 regular blocks; `run-2` contains 4 regular blocks.
    - `ses-2-meg`: data from participant's time in the MEG scanner. Contains `meg` and `behav` data from 4 'sessions' (i.e., `runs`) saved in separate csv files, each containing 4 blocks. `meg` and `behav` are recorded simultaneously.
    - Note that MEG data files with `.fif` extension are ignored and not on git.
    - `ses-3-structural`: data from participant structural MRI scan.
    - Note that MRI data files with `.nii` and `dcm` extension are ignored and not on git.
- `data_maxfiltered` contain the maxfiltered version of the raw MEG data. Current maxfilter settings are as follows:

  - [Multistage](https://github.com/OHBA-analysis/osl/tree/main/osl/maxfilter#multistage) setting is on.

  The multistage maxfilter is selected using `--mode multistage`. This will first run:

  1. Maxfilter with limited customisation, no movement compensation and autobad on to identify bad channels. Outputs `_autobad_sss.fif`
  2. Maxfilter with full customisation and movement compensation with the specific bad channels from stage 1. Outputs `_tsss.fif`
  3. Position translation (this requires that the `-trans` options are specified)

  ```

  --tsss                Apply temporal extension of maxfilter 
  --headpos             Output additional head movement parameter file  
  --movecomp            Apply movement compensation --trans TRANS         Transforms the data to the head position in defined file
  ```

- `docs` contains:

  - Four data-related docs.
    - `coinsmeg_counterbalancing.xlsx`: information about counterbalancing of key/button-action mapping, source-volability mapping, and blocks orders within runs ('sessions').
      - E.g., for sub-22, a/s keys (corresponding to buttons 1 & 2 in the MEG scanner) controlled clockwise/counterclockwise movement (respectively) of the shield, and k/l keys (buttons 3 & 4 in the MEG scanner) controlled decreasing/increasing shield size respectively.
    - `coinsmeg_if-data-exist.csv`: does this data exist at all? Headers contain relevant subdirectory paths.
      - If 'y', the data corresponding to this subdirectory exists even if it may not yet be in the directory.
      - If 'no', the data does not exist and we most likely cannot obtain it (i.e., for structurals, participant has left the country; no response despite multiple follow-ups).
      - If 'tbc', we have been in touch with people who say they have this data, but are still waiting on them to share it.
    - `coinsmeg_if-data-in-directory.csv`: is this data in the relevant subdirectory? ('y' = yes; 'n' = no)
    - `coinsmeg_participant_notes.xlsx`: any notes relating to this participant (e.g., any issues, truncated training due to participant lateness, internal number of the MEG scan denoted by #XXX).
  - Documentation that is not data-related is not yet in this repo. This includes participant screener responses, a password-protected linking document (linking participant names to IDs), and the study protocol (`coinsmeg_protocol.md`).

#### Current status

- A first preprocessing and ERF pipeline has been built for `sub-12`.
- All subjects/runs maxfiltered.

#### Participants with incomplete data

- The following subjects have existing anatomical scans, but we are still waiting on copies: 5, 6, 8, 22
- The following subjects do not have existing anatomical scans: 1, 2, 3


### Trigger information

Below are the trigger descriptors/labels, corresponding trigger values, and corresponding trigger meanings.

* expStart = 100; start of the experiment
* expEnd = 105; end of experiment

* lastFrame = 99; last frame of experiment
* practiceMove = 101; practiced moving shield

* practiceSize = 102; practiced changing shield size
* blockStart = 10; start of block (there were 4 blocks per run)

* blockEnd = 20; end of block
* laserHit = 1; a laser had hit the shield (i.e., the laser was successfully caught)

* laserMiss = 2; a laser had missed the shield
* keyRight = 3; key pressed to move shield to the right

* keyLeft = 4; key pressed to move shield to the left
* keyUp = 5; key pressed to make shield size larger

* keyDown = 6; key pressed to make shield size smaller
* keyRelease = 7; ?
