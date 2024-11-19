"""Coregistration and source reconstruction 
Created AXL 28/10/24

The script should be first run for all subjects. Then for subjects
whose coregistration looked a bit off we re-run this script just for that
particular subject.

This does not use OSL batch utils/config-file setup.
"""

############## ------- Import packages and define functions needed ---------- ############

import os
import os.path as op
import argparse
from pprint import pprint
import osl
from osl import utils
from osl import source_recon
import numpy as np
import coinsmeg_data as coinsmeg
from IPython.display import HTML, display
from glob import glob
import pathlib

import mne
from mne import read_forward_solution 

from osl.source_recon.rhino.polhemus import extract_polhemus_from_info
from osl.source_recon import rhino, beamforming, parcellation # for calculating beamformer weights

# functions
def copy_polhemus_files(polhemus_dir, recon_dir, subject):
    polhemus_headshape = np.loadtxt(op.join(polhemus_dir, 'polhemus_headshape.txt'))
    polhemus_nasion = np.loadtxt(op.join(polhemus_dir, 'polhemus_nasion.txt'))
    polhemus_rpa = np.loadtxt(op.join(polhemus_dir, 'polhemus_rpa.txt'))
    polhemus_lpa = np.loadtxt(op.join(polhemus_dir, 'polhemus_lpa.txt'))
    
    #  Get coreg filenames
    filenames = source_recon.rhino.get_coreg_filenames(recon_dir, subject)

    # Save
    np.savetxt(filenames["polhemus_nasion_file"], polhemus_nasion)
    np.savetxt(filenames["polhemus_rpa_file"], polhemus_rpa)
    np.savetxt(filenames["polhemus_lpa_file"], polhemus_lpa)
    np.savetxt(filenames["polhemus_headshape_file"], polhemus_headshape)

############## ------- Parse command-line arguments ---------- ############

parser = argparse.ArgumentParser(description="Run coregistration and source reconstruction for MEG data.")
parser.add_argument(
    '--parcellation_version', 
    default=coinsmeg.PARC_NAME,
    type=str, 
    required=False, 
    help="Specify the parcellation version to use for source reconstruction."
)
args = parser.parse_args()
# Setting of which parcellation file to use
parcellation_version = args.parcellation_version # eg 'HarvOxf-sub-Schaefer100-combined-2mm_4d_ds8'
parcellation_fname = f"{coinsmeg.DERIVATIVES_DIR}/recon/{parcellation_version}.nii.gz"

############## ------- Directories ---------- ############

# Directories
data_dir = coinsmeg.RAW_DIR # this is the same as BASE_DIR as raw data is stored in the base directory
preproc_dir = coinsmeg.PREPROCESSED_DIR
recon_dir = op.join(coinsmeg.DERIVATIVES_DIR, "recon")

# Get subjects
subs = []

data_sub_folders = sorted(filter(lambda path: "sub-" in path, glob(data_dir + '/*'))) # returns a list of paths e.g., '/ohba/pi/lhunt/datasets/coins-meg_data/sub-22'

for subject in data_sub_folders:
    subs.append(pathlib.Path(subject).stem) # subs is now a list of ['sub-01', 'sub-02', ...]

# Create a list with '_run-X' appended for each subject
sub_run_combos = []
for sub in subs:
    for run in range(1, 5):  # Loop from 1 to 4
        sub_run_combos.append(f"{sub}_run-{run}") # sub_run_combos is now a list of ['sub-01_run-1', 'sub-01_run-2', ...]

print(sub_run_combos) # eg ['sub-04_run-3'...]

############## -------  Run coregistration and source reconstruction   ---------- ############

for sub_run_combo in sub_run_combos:
    
    print(f"Starting coregistration and source reconstruction for {sub_run_combo}")

    # extract the subject and run id
    subject_id, run_id = sub_run_combo.split('_') # will produce subject_id = 'sub-XX', run_id = 'run-X'
    # set paths for where to look for necessary files
    anat_dir = coinsmeg.get_sub_anat_dir(subject_id)
    smri_file = f"{anat_dir}/{subject_id}_T1w.nii"
    fif_file = coinsmeg.get_sub_preproc_raw_fpath(subject_id, run_id)
    
    if not os.path.exists(smri_file):
        print(f"WARNING: smri_file does not exist for {sub_run_combo}!")
        continue # skip over the rest of the code for this sub_run_combo

    source_recon.rhino.compute_surfaces(
        smri_file,
        recon_dir,
        sub_run_combo,
        include_nose=True,
    )
    # check in fsleyes
    # source_recon.rhino.surfaces_display(recon_dir, sub_run_combo)
    
    polhemus_dir = op.join(recon_dir, sub_run_combo, "polhemus")
    # make directory if it doesn't yet exist
    os.makedirs(polhemus_dir, exist_ok=True)

    extract_polhemus_from_info(
        fif_file = fif_file,
        headshape_outfile=op.join(polhemus_dir, "polhemus_headshape.txt"),
        nasion_outfile=op.join(polhemus_dir, "polhemus_nasion.txt"),
        rpa_outfile=op.join(polhemus_dir, "polhemus_rpa.txt"),
        lpa_outfile=op.join(polhemus_dir, "polhemus_lpa.txt")
    )

    # recall that our maxfiltering options were
    # f"--maxpath /neuro/bin/util/maxfilter --mode multistage --scanner Neo --tsss --headpos --movecomp --trans {trans_file}",)
            #  the maxfilter aligns all runs of a participant so that the head position is the same within each participant
    
    copy_polhemus_files(polhemus_dir, recon_dir, sub_run_combo)

    # Then we run the coreg, for real.

    source_recon.rhino.coreg(
        fif_file, # full path to the MNE raw fif file
        recon_dir, # full path to the directory that contains the subject directories RHINO outputs
        sub_run_combo, # the name of the subject directories RHINO outputs to
        use_headshape=True,     #use the headshape points to refine the coregistration?
        use_nose=True, # use the nose headshape points to refine the coregistration?
    )

    # now view result
    source_recon.rhino.coreg_display(subjects_dir = "/ohba/pi/lhunt/datasets/coins-meg_data/derivatives/recon", 
                                    subject = sub_run_combo,
                                    filename = f"{recon_dir}/{sub_run_combo}/rhino/coreg/coreg_display_plot.html") # saves an interactive html plot at this location

    # Compute forward model
    gridstep = 10
    source_recon.rhino.forward_model(
        recon_dir,
        sub_run_combo,
        model="Single Layer",
        gridstep=gridstep,
    )

    # view results
    source_recon.rhino.bem_display(
        recon_dir,
        sub_run_combo,
        display_outskin_with_nose=False,
        display_sensors=True,
        plot_type="surf",
        filename=f"{recon_dir}/{sub_run_combo}/rhino/coreg/bem_display_plot.html",
    )

    # load forward solution
    fwd_fname = op.join(recon_dir, sub_run_combo, "rhino", "model-fwd.fif") 
    # tutorial said source_recon.rhino.get_coreg_filenames(recon_dir, subjects[0])["forward_model_file"]
    # but this did not return a match for "forward_model_file"
    print(fwd_fname)

    fwd = read_forward_solution(fwd_fname)
    leadfield = fwd["sol"]["data"]
    print("Leadfield size : %d sensors x %d dipoles" % leadfield.shape)

    # Temporal filtering

    chantypes = ["grad", "mag"] 

    # Get and setup the data
    data = mne.io.read_raw_fif(fif_file, preload=True)
    data = data.pick(chantypes)

    # Filter to the beta band
    print("Temporal Filtering")
    data = data.filter(
        l_freq=1,
        h_freq=30,
        method="iir",
        iir_params={"order": 5, "btype": "bandpass", "ftype": "butter"},
    )
    print("Completed")

    # Compute BEAMFORMER WEIGHTS
      
    # Make LCMV beamformer filters
    # Note that this will exclude any bad time segments when calculating the beamformer filters
    filters = beamforming.make_lcmv(
        recon_dir,
        sub_run_combo,
        data,
        chantypes,
        pick_ori="max-power-pre-weight-norm",
        rank={"meg": 60},
    )

    print("Applying beamformer spatial filters")

    # stc is source space time series (in head/polhemus space).
    stc = beamforming.apply_lcmv(data, filters)

    # Convert from head/polhemus space to standard brain grid in MNI space
    recon_timeseries_mni, reference_brain_fname, recon_coords_mni, _ = \
            beamforming.transform_recon_timeseries(recon_dir, 
                                                    sub_run_combo, 
                                                    recon_timeseries=stc.data, 
                                                    reference_brain="mni")

    print("Completed")
    print(f"Dimensions of reconstructed timeseries in MNI space is (dipoles x all_tpts) = {recon_timeseries_mni.shape}")

    # PARCELLATION

    print("Parcellating data")

    # Apply parcellation to (voxels x all_tpts) data contained in recon_timeseries_mni.
    # The resulting parcel_timeseries will be (parcels x all_tpts) in MNI space
    # where all_tpts includes bad time segments
    parcel_ts, _, _ = parcellation.parcellate_timeseries(
        parcellation_fname, # corresponds to the -beamform_and_parcellate: method: parcellation_file
        recon_timeseries_mni, # reconstructed timeseries in MNI space; dimensions are (dipoles x all_tpts)
        recon_coords_mni,  # dimensions are 3 x dipoles ((3, 2527)). the 3 rows are x, y, and z coordinates in MNI space
        "spatial_basis",  # corresponds to the -beamform_and_parcellate: method: setting
        recon_dir,
    )

    print("Completed")
    print(f"Dimensions of parcel timeseries in MNI space is (nparcels x all_tpts) = {parcel_ts.shape}")

    # Create mne raw object for the parcellated data

    # We reload raw data to ensure that the stim channel is in there
    raw = mne.io.read_raw_fif(fif_file) # recall that fif_file is a specific subject/run
    parc_raw = parcellation.convert2mne_raw(parcel_ts, raw)

    print(f"Dimensions of parc_raw are (nparcels x all_tpts) = {parc_raw.get_data().shape}")

    # source space data directory
    parc_dir = coinsmeg.get_sub_parc_dir(subject_id, run_id, parc_name=parcellation_version)
    os.makedirs(parc_dir, exist_ok=True)

    # save parc_raw into the src_dir
    parc_file = coinsmeg.get_sub_parc_fpath(subject_id, run_id, parc_name=parcellation_version)
    parc_raw.save(parc_file, overwrite=True)