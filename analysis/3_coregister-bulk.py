"""Coregisteration.

The scripts was first run for all subjects (with n_init=1). Then for subjects
whose coregistration looked a bit off we re-run this script just for that
particular subject with a higher n_init.

Note, these scripts do not include/use the nose in the coregistration.
If you want to use the nose you need to change the config to include the nose
and you may not want to call the remove_stray_headshape_points function.
"""

import numpy as np
from dask.distributed import Client

from osl import source_recon, utils
import coinsmeg_data as coinsmeg
import os

# Read in the data ####
sub = coinsmeg.sub_num2str(17) #  function sub_num2str converts a numerical subject identifier into a string formatted as sub-XX
run=1

# Directories

# Input dir - the preprocessed fif file + smri file
name = f"/{sub}_ses-2-meg_task-coinsmeg_run-{run}_meg-transsss" # name after maxfiltering 
preproc_file = os.path.join(coinsmeg.PREPROCESSED_DIR, name, f"/{name}_preproc_raw.fif")
anat_dir = coinsmeg.get_sub_anat_dir(sub)
smri_file = f"{anat_dir}/{sub}_T1w.nii"
coreg_dir = os.path.join(coinsmeg.BASE_DIR, "derivatives", "rhino", f"sub-{sub}")
print(coreg_dir)

# Subjects to coregister
# subjects = ["sub-04", "sub-07"] + [f"sub-{i:02d}" for i in range(9, 22)]
subjects = ["sub-12"] 
# Settings
config = """
    source_recon:
    - extract_polhemus_from_info: {}
    - remove_stray_headshape_points: {}
    - compute_surfaces:
        include_nose: False
    - coregister:
        use_nose: True 
        use_headshape: True
        #n_init: 50
"""

# use_nose:  = use the nose headshape points to refine the coregistration

if __name__ == "__main__":
    utils.logger.set_up(level="INFO")

    # Setup files
    preproc_files = []
    smri_files = []
    for subject in subjects:
        preproc_files.append(preproc_file.format(subject=subject))
        smri_files.append(smri_file.format(subject=subject))

    # Setup parallel processing
    #
    # n_workers is the number of CPUs to use,
    # we recommend less than half the total number of CPUs you have
    client = Client(n_workers=4, threads_per_worker=1)

    # Run coregistration
    source_recon.run_src_batch(
        config,
        src_dir=coreg_dir,
        subjects=subjects,
        preproc_files=preproc_files,
        smri_files=smri_files,
        dask_client=True,
    )
