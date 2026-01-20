from .core import File
from . import plotting


def read(filename, instrument=None):
    return File(filename, instrument=instrument)
