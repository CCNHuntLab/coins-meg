"""
Helper functions for parcels-based analyses using the glasser52 atlas.
"""

import coinsmeg_data as coinsmeg
import os
import pandas as pd

# Private variable to store the cached dataframe that contains the parcels
# information.
_cached_parcel_info = None

# File containing the parcel information
PARCEL_INFO_FPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "parcellation/glasser52/Parcel-Info.csv")

def get_parcel_info():
    """
    Returns a dataframe containing parcel information stored in the
    corresponding CSV file.

    On the first call, the CSV table is loaded and the resulting dataframe
    is cached and then returned. On subsequent, calls the cached dataframe
    is returned, avoiding the cost of loading the file.
    """
    global _cached_parcel_info
    if _cached_parcel_info is None:
        # Load the dataframe and cache it
        _cached_parcel_info = pd.read_csv(PARCEL_INFO_FPATH)
    return _cached_parcel_info

def get_parcel_idx_with_name(fullname):
    parcel_info = get_parcel_info()
    return parcel_info.loc[parcel_info["Parcel-Name"] == fullname, "Parcel-Idx"].iloc[0]

def get_parcel_idx_with_names(fullnames):
    return [get_parcel_idx_with_name(fullname) for fullname in fullnames]

def get_parcel_idx_with_name_hemi(name, hemi):
    fullname = f"{name}_{hemi}"
    return get_parcel_idx_with_name(fullname)

def get_parcel_idx_with_name_2hemi(name):
    return [get_parcel_idx_with_name_hemi(name, hemi) for hemi in ["rh", "lh"]]

def get_parcel_idx_with_names_2hemi(names):
    return [parcel_idx for name in names for parcel_idx in get_parcel_idx_with_name_2hemi(name)]

def get_parcel_names_2hemi(names):
    return [f"{name}_{hemi}" for name in names for hemi in ["rh", "lh"]]

def get_parcel_img(parc_name=coinsmeg.PARC_NAME):
    # This nifti image file must be added to the below folder.
    # It can be downloaded from the parcellation dataset at:
    # https://zenodo.org/records/11099418
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
        f"parcellation/glasser52/{parc_name}.nii.gz")

def get_pretty_name(name):
    if name.endswith("_rh"):
        return f"""Right {name.rstrip("_rh")}"""
    elif name.endswith("_lh"):
        return f"""Left {name.rstrip("_lh")}"""
    else:
        return name