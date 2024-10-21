"""
Module for TRF (Temporal Response Function) estimation.
"""

import cf_utils as utils
import coinsmeg_data as coinsmeg
import mne
import numpy as np
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
    Ykeys = DATA_TYPES
    Xs = []
    Ys = {k: [] for k in Ykeys}
    sfreq = None
    for run in runs:
        XY = get_XY_singlerun(sub, run, event_names,
            **kwargs)
        Xs += [XY["X"]]
        for k, v in XY["Y"].items():
            Ys[k] += [v]
        if sfreq is None:
            sfreq = XY["sfreq"]
    return {
        "X": np.concatenate(Xs, axis=0),
        "Y": {k: np.concatenate(Ys[k], axis=0) for k in Ykeys},
        "sfreq": sfreq
    }


def get_XY_singlerun(sub, run, event_names,
    do_locally=False,
    tmin=-0.5, tmax=1.0,
    downsamp=10, downsamp_method="resample",
    no_reject=False):
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
    # File paths to the data for the given subject and run
    paths = {}
    paths["sensorspc"] = coinsmeg.get_sub_preproc_raw_fpath(sub, run)
    paths["sourcespc"] = coinsmeg.get_sub_src_parc_fpath(sub, run)
    if do_locally:
        for k, fpath in paths.items():
            paths[k] = fpath.replace(coinsmeg.BASE_DIR, utils.LOCAL_BASE_DIR)

    # Get sensor-space and source-space data as MNE.Raw objects
    raws = {}
    raws["sensorspc"] = mne.io.read_raw_fif(paths["sensorspc"])
    raws["sourcespc"] = mne.io.read_raw(paths["sourcespc"])

    srcspace_info = raws["sourcespc"].info
    original_sfreq = srcspace_info["sfreq"]
    sfreq = original_sfreq / downsamp

    # Resample the data if requested
    if downsamp != 1 and downsamp_method == "resample":
        for k, raw in raws.items():
            raws[k] = raw.resample(sfreq)

    # Factor to decimate the data if requested
    decim = downsamp if (downsamp_method == "decimate" and downsamp != 1) else None

    # Find the indices corresponding to the parcels data vs the stim channel
    # in the source-space raw data array
    i_all_parcels = mne.pick_types(srcspace_info, misc=True)
    i_stim = mne.pick_types(srcspace_info, stim=True)[0]

    # Load the MEG data and create the corresponding Y arrays
    data = {}
    reject_by_annotation = None if no_reject else "NaN"
    data["parcels"] = raws["sourcespc"].get_data(i_all_parcels, 
        reject_by_annotation=reject_by_annotation)[:, ::decim] # shape (n_parcels, n_samples)
    for k in ["mag", "grad"]:
        data[k] = raws["sensorspc"].get_data(picks=k,
            reject_by_annotation=reject_by_annotation)[:, ::decim] # shape (n_channels, n_samples)
    Y = {}
    for k in DATA_TYPES:
        Y[k] = data[k].T

    # Load the stimulus event data and create the corresponding X array,
    # focusing on the given events of interest.
    ev_ids = [coinsmeg.EVENT_ID[fn] for fn in event_names]
    stim = raws["sourcespc"].get_data([i_stim],
        reject_by_annotation=reject_by_annotation)[0][::decim] # shape (n_samples, )
    X = np.stack([(stim == ev_id) for ev_id in ev_ids],
        axis=1).astype(float) # shape (n_samples, n_features)

    return {"X": X, "Y": Y, "sfreq": sfreq}

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

def calculate_rms_trf(trf_model):
    """
    Calculate the RMS across sensors of the beta coefficients,
    mirroring the behavior of mne.viz.plot_compare_evokeds(),
    so that we can compare with Epoched ERFs.
    """
    return np.sqrt((trf_model.coef_ ** 2).mean(axis=0))
    