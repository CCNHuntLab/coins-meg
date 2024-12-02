"""Module for common code shared between subject- and group-level TRF analyses."""

import cf_parcellation
import matplotlib as mpl
import matplotlib.pyplot as plt
import mne
import nilearn.image
import nilearn.plotting

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

def plot_parcels_timecourse(evoked, parcel_indices, parcel_names,
    ax=None, do_legend=True, do_color=True, highlight=None, 
    xlabel="Time (s)", ylabel="AU", title=None, lw=1.,
    colors=None):
    if ax is None:
        fig = plt.figure(figsize=(6.4, 3))
        ax = fig.gca()
    else:
        fig = ax.get_figure()
    if colors is None:
        cmap = mpl.colormaps.get_cmap("tab20")
        colors = [cmap(i) if do_color else "black" for i in range(len(parcel_indices))]
    for i in range(len(parcel_indices)):
        ax.plot(evoked.times, evoked.data[parcel_indices[i], :],
            label=parcel_names[i], color=colors[i], lw=lw)
    if do_legend:
        ax.legend()
    if highlight is not None:
        ylim = ax.get_ylim()
        ax.fill_betweenx(ylim, highlight[0], highlight[1],
            facecolor="orange", alpha=0.15)
        ax.set_ylim(ylim)
    ax.set_xlim(evoked.times[0], evoked.times[-1])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    return fig

def plot_parcel_location(parcel_idx, parcel_name,
    ax=None, color=None, title=None):
    if ax is None:
        fig = plt.figure(figsize=(6.4, 2))
        ax = fig.gca()
    else:
        fig = ax.get_figure()
    if color is None:
        color = mpl.colormaps.get_cmap("Set1")(4)
    cmap_binary_img = mpl.colors.LinearSegmentedColormap.from_list(
        "cmap_binary_img", [(0, 0, 0), color])
    fpath = cf_parcellation.get_parcel_img()
    parcel_img = nilearn.image.index_img(fpath, parcel_idx)
    binary_parcel_img = nilearn.image.binarize_img(parcel_img, threshold=0.25,
        two_sided=False)
    display = nilearn.plotting.plot_roi(binary_parcel_img,
        cmap=cmap_binary_img, vmin=0, axes=ax, figure=fig,
        black_bg=False, annotate=False)
    display.annotate(size=mpl.rcParams['font.size'])
    if title:
        display.title(title, size=mpl.rcParams['figure.titlesize'], color="black",
            bgcolor="white", ha="center", va="top", x=0.5, y=0.99)
    return fig
