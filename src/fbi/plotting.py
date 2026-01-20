from matplotlib import pyplot as plt
import numpy as np


def plot_ccf_mask(wavelength, contrast, ax=None, offset=0):
    """
    Plot a CCF mask as vertical lines going from 0 down to -contrast.

    Parameters
    ----------
    wavelength : array-like
        Mask line wavelengths.
    contrast : array-like
        Line contrasts (positive numbers).
    ax : matplotlib axis, optional
        If provided, draw on this axis.
    """
    wavelength = np.asarray(wavelength)
    contrast = np.asarray(contrast)

    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 4))

    # vertical line for each mask line
    ax.vlines(wavelength, ymin=0+offset, ymax=-
              contrast+offset, color='k', linewidth=0.8)

    ax.set_xlabel("Wavelength")
    ax.set_ylabel("Contrast")
    ax.set_title("CCF Mask")

    # Optional: invert y-axis so lines point downward naturally

    return ax
