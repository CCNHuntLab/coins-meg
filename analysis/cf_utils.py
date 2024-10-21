"""
Utility functions for analysis scripts
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import os.path as op

LOCAL_BASE_DIR = "/Users/cedric/Code_and_Repositories/ContInf_-_Code/coins-meg_data"

#
# Saving outputs
#

def create_dir_if_needed(d):
    if not op.exists(d):
        os.makedirs(d, exist_ok=True)

def name_with_params(prefix, keys, vals):
    name = prefix
    for key, val in zip(keys, vals):
        if ((val is not None)
            and (val is not False)):
            if type(val) == bool:
                name += f"_{key}"
            else:
                name += f"_{key}-{val}"
    return name

def path_with_components(dir, basename, ext="png"):
    fname = f"{basename}.{ext}"
    return op.join(dir, fname)

def save_figure(fig, figpath, verbose=True):
    fig.savefig(figpath)
    plt.close(fig)
    if verbose:
        print(f"Figure saved at {figpath}")

#
# Plotting 
#

# Constants
A4_PAPER_CONTENT_WIDTH = 7.1
DEFAULT_HEIGHT = 2.16

# Default values for various plotting style settings
def setup_mpl_style(fontsize=8):
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = 'Arial'
    mpl.rcParams['mathtext.default'] = 'regular'
    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['font.size'] = fontsize
    mpl.rcParams['figure.titlesize'] = fontsize
    mpl.rcParams['axes.titlesize'] = fontsize
    mpl.rcParams['axes.labelsize'] = fontsize
    mpl.rcParams['xtick.labelsize'] = fontsize
    mpl.rcParams['ytick.labelsize'] = fontsize
    mpl.rcParams['legend.fontsize'] = fontsize-1
    mpl.rcParams['axes.labelpad'] = 4.0
    mpl.rcParams['lines.linewidth'] = 1.0
    mpl.rcParams["legend.frameon"] = False
    mpl.rcParams['figure.constrained_layout.use'] = True
