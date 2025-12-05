# registry.py
PARSERS = []


def register_parser(parser_class):
    PARSERS.append(parser_class)
    return parser_class
