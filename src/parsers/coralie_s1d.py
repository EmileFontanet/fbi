from parsers.registry import register_parser
from parsers.utils import coralie_s1d_wavelength_solution


@register_parser
class CoralieS1DParser:

    @classmethod
    def can_parse(cls, header, fname):
        return (
            header.get("INSTRUME") == "CORALIE"
            and "s1d" in fname.lower()
        )

    def __init__(self, hdul):
        self.hdul = hdul
        drs_version = hdul[0].header.get("HIERARCH ESO DRS VERSION", "unknown")
        drs_version = drs_version.replace("CORALIE_", "")
        if drs_version in ['3.3', '3.4', '3.8']:
            # Case of CORALIE old DRS
            self.flux = hdul[0].data
            self.wave_air = coralie_s1d_wavelength_solution(hdul[0].header)
            self.wave = None
            self.err = None
        else:
            # Case of CORALIE new DRS
            self.flux = hdul[1].data['flux']
            self.err = hdul[1].data['error']
            self.wave = hdul[1].data['wavelength']
            self.wave_air = hdul[1].data['wavelength_air']
