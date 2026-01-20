import numpy as np


def doppler_shift(wave: np.ndarray, rv: float) -> np.ndarray:
    """
    Performs the doppler shift on the wavelength values.

    Args:
        wave (np.ndarray): the original wavelength values
        rv (float): the radial velocity of the object in km/s

    Returns:
        wave_shifted (np.ndarray): the doppler shifted wavelength values
    """
    from astropy.constants import c

    wave_shifted = wave + wave * rv / (c / 1e3).value
    return wave_shifted
