"""
Module for TRF (Temporal Response Function) estimation.
"""

import cf_utils as utils
import coinsmeg_data as coinsmeg
import mne
import numpy as np
import os.path as op
import sklearn.linear_model

DATA_TYPES = ["parcels", "mag", "grad"]

class RidgeWithNan(sklearn.linear_model.Ridge):
    """Subclass of scikit-learn's Ridge estimator that can handle NaN values
    in the data. The strategy for dealing with NaNs is to discard rows
    from X and Y where a NaN value is present in either X or Y."""

    def _nan_rows(self, X):
        if X.ndim == 2:
            return np.isnan(X).any(axis=1)
        elif X.ndim == 1:
            return np.isnan(X)

    def _remove_nan(self, X, Y):
        # Find the row indices where there is a NaN value in either X or Y
        assert X.ndim == 2 and Y.ndim == 2
        nan_rows = self._nan_rows(X) | self._nan_rows(Y)
        # Filter out the rows with NaN values
        X = X[~nan_rows]
        Y = Y[~nan_rows]
        return X, Y

    def fit(self, X, y, sample_weight=None):
        X, y = self._remove_nan(X, y)
        return super().fit(X, y, sample_weight=sample_weight)

    def score(self, X, y, sample_weight=None):
        X, y = self._remove_nan(X, y)
        return super().score(X, y, sample_weight=sample_weight)


def get_XY(sub, event_names, runs=coinsmeg.RUNS, **kwargs):
    """
    Create X and Y arrays for the TRF estimation with the given subject across
    all the given runs. These is simply the concatenation of the corresponding
    arrays for each run.

    See get_XY_singlerun() for more details on the X and Y, and the parameters
    and return value of this function.
    """
    Xs = []
    Ys = None
    Y_info = None
    for run in runs:
        XY = get_XY_singlerun(sub, run, event_names,
            **kwargs)
        Xs += [XY["X"]]
        if Ys is None:
            Ykeys = XY["Y"].keys()
            Ys = {k: [] for k in Ykeys}
        for k, v in XY["Y"].items():
            Ys[k] += [v]
        if Y_info is None:
            Y_info = XY["Y_info"]
    return {
        "X": np.concatenate(Xs, axis=0),
        "Y": {k: np.concatenate(Ys[k], axis=0) for k in Ys.keys()},
        "Y_info": Y_info
    }


def get_XY_singlerun(sub, run, event_names,
    do_locally=False,
    tmin=-0.5, tmax=1.0,
    downsamp=10, downsamp_method="resample",
    no_reject=False,
    spaces=["sensor", "source"]):
    """
    Create X and Y arrays for the TRF estimation with the given subject and run./
    
    X (the design matrix) is a matrix of shape (n_samples, n_events),
    where n_events correspond to each event type for which we want to
    estimate a TRF.
    
    For each data type, Y is a matrix of shape (n_samples, n_channels) where n_channels
    corresponds either to the number of sensors when working in sensor space,
    or to the number of parcels when working in parcellated source space.

    Parameters
    ----------
    sub: int
        subject id
    run: int
        run number
    event_names: list of str
        list of event names for each event to include in the design matrix
    do_locally: bool
        Whether we are running the analysis locally, with a copy of the data
        stored on our machine, or on the server with access to /ohba/pi/lhunt,
        where the data is stored.
    tmin, tmax: floats
        Time window for the TRF
    downsamp: int or float
        Downsampling factor to use for the TRF estimation (this saves memory and
        compute time, but also improves statistical estimation due to decreasing
        the number of beta coefficients to estimate).
    downsamp_method: str
        "resample" or "decimate". When "resample", the data is resampled using
        MNE's resample function. When "decimate", the data is decimated by
        simply taking every nth sample in the data (where n == downsamp).
    no_reject: bool
        Whether to reject or skip rejecting bad segments, as defined by annotations
        in the MNE.Raw data objects.

    Returns
    -------
    XY: dict
        XY["X"]: the design matrix, as a numpy array.
        XY["Y"]: dictionary of of numpy arrays, one for each data type.
        XY["sfreq"]: sampling frequency
    """
    if spaces is None or len(spaces) == 0:
        return None

    # File paths to the data for the given subject and run
    paths = {}
    if "sensor" in spaces:
        paths["sensorspc"] = coinsmeg.get_sub_preproc_raw_fpath(sub, run)
    if "source" in spaces:
        paths["sourcespc"] = coinsmeg.get_sub_parc_fpath(sub, run)
    if do_locally:
        for k, fpath in paths.items():
            paths[k] = utils.get_local_path_for_data(fpath)

    # Get sensor-space and source-space data as MNE.Raw objects
    raws = {}
    if "sensor" in spaces:
        raws["sensorspc"] = mne.io.read_raw_fif(paths["sensorspc"])
    if "source" in spaces:
        raws["sourcespc"] = mne.io.read_raw(paths["sourcespc"])

    info = raws["sourcespc"].info if "source" in spaces else raws["sensorspc"].info
    original_sfreq = info["sfreq"]
    sfreq = original_sfreq / downsamp

    # Resample the data if requested
    if downsamp != 1 and downsamp_method == "resample":
        for k, raw in raws.items():
            raws[k] = raw.resample(sfreq)

    # Factor to decimate the data if requested
    decim = downsamp if (downsamp_method == "decimate" and downsamp != 1) else None

    # Find the indices corresponding to the parcels data vs the stim channel
    # in the source-space raw data array
    if "source" in spaces:
        i_all_parcels = mne.pick_types(info, misc=True)
        i_stim = mne.pick_types(info, stim=True)[0]

    # Load the MEG data and create the corresponding Y arrays
    data = {}
    reject_by_annotation = None if no_reject else "NaN"
    if "source" in spaces:
        data["parcels"] = raws["sourcespc"].get_data(i_all_parcels, 
            reject_by_annotation=reject_by_annotation)[:, ::decim] # shape (n_parcels, n_samples)
    if "sensor" in spaces:
        for k in ["mag", "grad"]:
            data[k] = raws["sensorspc"].get_data(picks=k,
                reject_by_annotation=reject_by_annotation)[:, ::decim] # shape (n_channels, n_samples)
    Y = {}
    for k in data.keys():
        Y[k] = data[k].T

    # Load the stimulus event data and create the corresponding X array,
    # focusing on the given events of interest.
    ev_ids = [coinsmeg.EVENT_ID[fn] for fn in event_names]
    if "source" in spaces:
        stim = raws["sourcespc"].get_data([i_stim],
            reject_by_annotation=reject_by_annotation)[0][::decim] # shape (n_samples, )
    else:
        stim = raws["sensorspc"].get_data(picks="stim",
            reject_by_annotation=reject_by_annotation)[0][::decim] # shape (n_samples, )
    X = np.stack([(stim == ev_id) for ev_id in ev_ids],
        axis=1).astype(float) # shape (n_samples, n_features)

    # Construct info object for each data type
    Y_info = {}
    for k in Y.keys():
        if k == "parcels":
            rawinfo = raws["sourcespc"].info
            i_channels =  i_all_parcels
        elif k in ["mag", "grad"]:
            rawinfo = raws["sensorspc"].info
            i_channels = mne.pick_types(rawinfo, meg=k)
        ch_names = [rawinfo.ch_names[i] for i in i_channels]
        ch_types = rawinfo.get_channel_types(i_channels)
        newinfo = mne.create_info(
            ch_names=ch_names,
            sfreq=sfreq,
            ch_types=ch_types,
        )
        # Set channel information, including channel locations
        for i_newinfo, i_rawinfo in enumerate(i_channels):
            newinfo["chs"][i_newinfo].update(rawinfo["chs"][i_rawinfo])
        # Set other info entries that should be manually changed by the user (as per MNE documentation)
        for infokey in ["bads", "device_info", "dev_head_t", "experimenter", "helium_info",
            "line_freq", "subject_info"]:
            if infokey in rawinfo.keys():
                newinfo[infokey] = rawinfo[infokey]
        if k in ["mag", "grad"]:
            newinfo.set_montage(rawinfo.get_montage())
        Y_info[k] = newinfo

    return {"X": X, "Y": Y, "Y_info": Y_info}

def plot_design_matrix(X, event_names):
    """Plot the given design matrix."""
    import nilearn.plotting
    import pandas as pd
    # nilearn can plot the design matrix when it is formatted as a dataframe,
    # with columns corresponding features, and rows corresponding to samples.
    design_matrix = pd.DataFrame(X, columns=event_names)
    return nilearn.plotting.plot_design_matrix(design_matrix)

def create_trf_model(event_names, sfreq, tmin=-0.5, tmax=1.0,
    no_reject=False, alpha=0):
    """Create the model for the TRF estimation."""
    estimator = (alpha if no_reject else RidgeWithNan(
                alpha=alpha, fit_intercept=True))
    return mne.decoding.ReceptiveField(tmin, tmax, sfreq,
                feature_names=event_names, estimator=estimator)

def estimate_trfs(trf_model, X, Y, Y_info):
    """Estimate the TRFs by fitting the TRF model to the given X and Y data.
    The TRFs are returned as a list of mne.Evoked instances, with one evoked
    response per feature/event in the design matrix X."""
    trf_model.fit(X, Y)
    trfs = [ mne.EvokedArray(
            trf_model.coef_[:, i_feat, :],
            Y_info,
            tmin=trf_model.tmin,
            comment=feat_name)
        for i_feat, feat_name in enumerate(trf_model.feature_names)
    ]
    return trfs

def save_trfs(trfs, fpath, verbose=True):
    """
    Save the TRFs to a file at the given fpath.
    The TRFs should be a list of mne.Evoked instances. The info objects of the
    TRFs should be all the same, as required by mne.write_evokeds(), which only
    uses the info of the first instance to write the file.
    The file path is a fif file whose name should end with '_ave' or '-ave' with
    extension '.fif' or '.fif.gz'.
    """
    mne.write_evokeds(fpath, trfs, overwrite=True)
    if verbose:
        print(f"TRFs saved at {fpath}")

def load_trfs(fpath, do_check_if_exists=True):
    """
    Load the TRFs from a .fif file at the given fpath. The TRFs are returned as
    a list of mne.Evoked instances.
    """
    if do_check_if_exists and (not op.exists(fpath)):
        return None
    return mne.read_evokeds(fpath)

def get_trfs_fname(sub, events, datatype,
    downsamp=10, downsamp_method="decimate", alpha=0, no_reject=False):
    downsamp_name = "downsamp" if (downsamp_method == "resample") else "decim"
    paramkeys = ["sub", "events", "datatype", downsamp_name, "alpha", "no-reject"]
    paramvals = [sub, events, datatype, downsamp, alpha, no_reject]
    fname = utils.name_with_params("trfs", paramkeys, paramvals)
    fname += "_ave" # MNE recommends the file name to end with "ave" for evoked instances
    return fname

def get_trfs_fpath(dir, sub, events, datatype,
    downsamp=10, downsamp_method="decimate", alpha=0, no_reject=False):
    trfs_fname = get_trfs_fname(sub, events, datatype,
        downsamp=downsamp, downsamp_method=downsamp_method,
        alpha=alpha, no_reject=no_reject)
    return utils.path_with_components(dir, trfs_fname, "fif")

def calculate_rms_trf(trf_model_coef):
    """
    Calculate the RMS across sensors of the beta coefficients,
    mirroring the behavior of mne.viz.plot_compare_evokeds(),
    so that we can compare with Epoched ERFs.
    """
    return np.sqrt((trf_model_coef ** 2).mean(axis=0))
    