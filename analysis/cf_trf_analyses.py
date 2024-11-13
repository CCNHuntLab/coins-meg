"""Module for common code shared between subject- and group-level TRF analyses."""

import mne

def compute_evoked_response(evoked_by_ev, effect, signaltype,
    baseline_window=(-0.2, 0.)):
    """
    Compute the evoked response for a given effect and signal type.

    Parameters
    ----------
    evoked_by_ev : dict
        Dictionary containing the evoked responses to events from which the effects
        are computed.
    effect : str
        Effect to compute the evoked response for.
    signaltype : str
        Type of value to compute from the original signal. Can be:
        - signal: The original, untouched signal value.
        - rel-signal: The signal value relative to baseline (signal - baseline).
          The baseline is computed by averaging the signal over the specified
          baseline period.
        - z-signal: The z-scored signal value. The mean and std used for the
          z-scoring are the mean and std of the signal in the baseline period.

    Returns
    -------
    evoked : mne.Evoked
        The computed evoked response.
    """
    # First, compute the evoked response for the given effect
    # by computing the relevant contrast (i.e. weighted sum) of the
    # responses to single events.
    event_names = evoked_by_ev.keys()
    if effect in evoked_by_ev:
        evoked = evoked_by_ev[effect].copy()
    else:
        if effect == "laserMiss-minus-laserHit":
            weights = [-1, +1]
        elif effect == "laserMiss-plus-laserHit":
            weights = [+1, +1]
        evoked = mne.combine_evoked(
            [evoked_by_ev["laserMiss"], evoked_by_ev["laserHit"]],
            weights)
    # Then, compute the relative or z-scored signal value,
    # using the baseline period to compute the mean and std used for
    # rescaling.
    do_baseline = "rel" in signaltype or "z" in signaltype
    do_z = ("z" in signaltype)
    baseline_mode = "zscore" if do_z else "mean"
    if do_baseline:
        evoked.data = mne.baseline.rescale(evoked.data, evoked.times,
            baseline_window, mode=baseline_mode)
        evoked.baseline = baseline_window
    return evoked
