from .core import File


def read(filename, instrument=None):
    return File(filename, instrument=instrument)
