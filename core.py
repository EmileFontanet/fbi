import astropy.io.fits as fits


class File:
    def __init__(self, filename, instrument=None, file_type=None, drs=None):
        self.filename = filename
        self._hdul = fits.open(filename, memmap=True)
        self.hdul = self._hdul
        self.file_type = file_type
        self._in_context = False

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
        return self._data

    @property
    def wave(self):
        return self._wave

    # --- instrument inference ---
    def _infer_instrument(self):
        with fits.open(self.filename, memmap=True) as hdul:
            header = hdul[0].header
            if "INSTRUME" in header:
                return header["INSTRUME"]
            elif "TELESCOP" in header:
                return header["TELESCOP"]
            else:
                return "GENERIC"

    def _infer_type(self):
        # --- instrument-specific extraction ---
        return

    def _infer_drs(self):
        # --- instrument-specific extraction ---
        return

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
    self.read_file(self):
