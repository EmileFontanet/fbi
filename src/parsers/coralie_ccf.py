from parsers.registry import register_parser
from parsers.utils import coralie_ccf_rv_array


@register_parser
class CoralieCCFParser:

    @classmethod
    def can_parse(cls, header, fname):
        return (
            header.get("INSTRUME") == "CORALIE"
            and "ccf" in fname.lower()
        )

    def __init__(self, hdul):
        self.hdul = hdul
        drs_version = hdul[0].header.get("HIERARCH ESO DRS VERSION", "unknown")
        drs_version = drs_version.replace("CORALIE_", "")
        if drs_version in ['3.3', '3.4', '3.8']:
            # Case of CORALIE old DRS
            self.flux = hdul[0].data
            self.rv_arr = coralie_ccf_rv_array(hdul[0].header,
                                               nb_points=self.flux.shape[1],
                                               drs='odrs')
            self.err = None
        else:
            # Case of CORALIE new DRS
            self.flux = hdul['SCIDATA'].data
            self.err = hdul['ERRDATA'].data
            self.rv_arr = coralie_ccf_rv_array(hdul[0].header,
                                               nb_points=self.flux.shape[1],
                                               drs='ndrs')
