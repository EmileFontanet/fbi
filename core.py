import astropy.io.fits as fits


class File:
    def __init__(self, filename, instrument=None):
        self.filename = filename
        self.instrument = instrument
        self.hdul = None

    def __enter__(self):
        """Open fits file."""
        self.hdul = fits.open(self.filename, memmap=True)
        self._parse()   # Extract wave, data, etc. automatically
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close fits file automatically."""
        if self.hdul is not None:
            self.hdul.close()

    # --- user-friendly attributes ---
    @property
    def header(self):
        return self.hdul[0].header if self.hdul else None

    @property
    def data(self):
        return self._data

    @property
    def wave(self):
        return self._wave

    # --- instrument-specific extraction ---
    def _parse(self):
        if self.instrument == "CORALIE":
            self._parse_coralie()
        elif self.instrument == "HARPS":
            self._parse_harps()
        else:
            self._parse_generic()

    def _parse_coralie(self):
        self._data = self.hdul["SCI"].data
        self._wave = self.hdul["WAVE"].data

    def _parse_harps(self):
        self._data = self.hdul[1].data
        self._wave = self.hdul[2].data

    def _parse_generic(self):
        self._data = self.hdul[0].data
        self._wave = None
