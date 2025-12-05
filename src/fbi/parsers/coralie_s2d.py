from fbi.parsers.registry import register_parser
from fbi.parsers.utils import coralie_s2d_wavelength_solution


@register_parser
class CoralieS2DParser:

    @classmethod
    def can_parse(cls, header, fname):
        return (
            header.get("HIERARCH ESO OBS INSTRUMENT") == "CORALIE"
            and ("e2ds" in fname.lower() or "s2d" in fname.lower()
                 ))

    def __init__(self, hdul, fname):
        self.hdul = hdul
        if "r." not in fname:
            # Case of CORALIE old DRS
            self.flux = hdul[0].data
            self.wave_air = coralie_s2d_wavelength_solution(hdul[0].header)
            self.wave = None
            self.err = None
        else:
            # Case of CORALIE new DRS
            self.flux = hdul['scidata'].data
            self.err = hdul['ERRDATA'].data
            self.wave = hdul['WAVEDATA_VAC_BARY'].data
            self.wave_air = hdul['WAVEDATA_AIR_BARY'].data
