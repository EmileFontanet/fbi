import astropy.io.fits as fits
from fbi.parsers.registry import PARSERS


class File:
    def __init__(self, filename, instrument=None, file_type=None, drs=None):
        self.filename = filename
        self.hdul = None

        # Automatically open the file outside a context manager
        self._open()

        # Choose the correct parser
        header = self.hdul[0].header
        self.parser = None

        for parser_cls in PARSERS:
            if parser_cls.can_parse(header, filename):
                self.parser = parser_cls(self.hdul, filename)
                break

        if self.parser is None:
            raise ValueError("No parser found for this file type.")

    def _open(self):
        if self.hdul is None:
            self.hdul = fits.open(self.filename)

    def close(self):
        if self._hdul is not None:
            self._hdul.close()
            self._hdul = None

    # Context manager support
    def __enter__(self):
        self._in_context = True
        return self

    def __exit__(self, exc_type, exc, tb):
        # Close only when used in "with"
        self.close()
        self._in_context = False

    # --- user-friendly attributes ---

    @property
    def header(self):
        return self.hdul[0].header if self.hdul else None

    @property
    def data(self):
        return self.parser.flux

    @property
    def wave(self):
        return self.parser.wave

    @property
    def wave_air(self):
        return self.parser.wave_air

    @property
    def rv_arr(self):
        return getattr(self.parser, 'rv_arr', None)

    @property
    def err(self):
        return self.parser.err
