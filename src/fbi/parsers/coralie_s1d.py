from fbi.parsers.registry import register_parser
from fbi.parsers.utils import coralie_s1d_wavelength_solution


@register_parser
class CoralieS1DParser:

    @classmethod
    def can_parse(cls, header, fname):
        return (
            header.get("HIERARCH ESO OBS INSTRUMENT") == "CORALIE"
            and "s1d" in fname.lower()
        )

    def __init__(self, hdul, fname):
        self.hdul = hdul

        if "r." not in fname:
            # Case of CORALIE old DRS
            self.flux = hdul[0].data
            self.wave_air = coralie_s1d_wavelength_solution(hdul[0].header)
            self.wave = None
            self.err = None
            print('Finished loading S1d')
        else:
            # Case of CORALIE new DRS
            self.flux = hdul[1].data['flux']
            self.err = hdul[1].data['error']
            self.wave = hdul[1].data['wavelength']
            self.wave_air = hdul[1].data['wavelength_air']
