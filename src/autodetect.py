# autodetect.py
from parsers.registry import PARSERS


def detect_parser(hdul):
    for parser_class in PARSERS:
        if parser_class.can_handle(hdul):
            return parser_class(hdul)

    raise ValueError("No parser found for this FITS file")
