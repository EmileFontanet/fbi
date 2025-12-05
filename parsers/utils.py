import numpy as np


def coralie_s2d_wavelength_solution(header):
    """
        Get the wavelength solutions for CORALIE e2ds files.
        header: Header of the e2ds fits file
    """
    nb_pixel = header['NAXIS1']
    order_max = header['NAXIS2']
    wave = np.zeros((order_max, nb_pixel))
    pixel_pos_A = np.array(list(np.arange(nb_pixel))
                           * order_max).reshape((order_max, nb_pixel))

    for k in np.arange(order_max):
        x = pixel_pos_A[k]
        for j in range(5):
            wave[k] += header[f'ESO DRS CAL TH COEFF LL{5 * k + j}'] * x ** j

    return wave


def coralie_s1d_wavelength_solution(header):
    """
        Get the wavelength solutions for CORALIE s1d files.
        header: Header of the s1d fits file
    """
    wave = np.linspace(header['CRVAL1'],
                       header['CRVAL1']+(header['NAXIS1']-1)*header['CDELT1'],
                       header['NAXIS1'])
    return wave


def coralie_ccf_rv_array(header, nb_points, drs='ndrs'):
    """
        Get the RV array for CORALIE CCF files.
        header: Header of the CCF fits file
        nb_points: Number of points in the CCF
        drs: 'odrs' for old DRS, 'ndrs' for new DRS
    """
    if drs == 'odrs':
        rv_start = header['CRVAL1']
        rv_step = header['CDELT1']
    elif drs == 'ndrs':
        rv_start = header['HIERARCH ESO RV START']
        rv_step = header['HIERARCH ESO RV STEP']

    rv_array = rv_start + rv_step * np.arange(nb_points)
    return rv_array
