from fbi.parsers.registry import register_parser


@register_parser
class HarpsS2DParser:

    @classmethod
    def can_parse(cls, header, fname):
        return (
            header.get("INSTRUME") == "HARPS"
            and "s2d" in fname.lower()
        )

    def __init__(self, hdul, fname):
        self.hdul = hdul

        if "r." not in fname:
            raise NotImplementedError(
                "HARPS old DRS S1D files are not supported.")
        else:
            # Case of CORALIE new DRS
            self.ftype = 'HARPS_S2D'
            self.berv_corrected = True
            self.flux = hdul['scidata'].data
            self.err = hdul['ERRDATA'].data
            self.wave = hdul['WAVEDATA_VAC_BARY'].data
            self.wave_air = hdul['WAVEDATA_AIR_BARY'].data
            self.berv = hdul['primary'].header.get('HIERARCH ESO QC BERV')
            self.vsys = hdul['primary'].header.get(
                'HIERARCH ESO TEL TARG RADVEL')
            self.vsys_corrected = False
