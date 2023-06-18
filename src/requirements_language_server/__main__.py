r"""This module can be called by
`python -m <https://docs.python.org/3/library/__main__.html>`_.
"""
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from contextlib import suppress
from datetime import datetime

from . import PATH
from . import __name__ as NAME
from . import __version__

NAME = NAME.replace("_", "-")
VERSION = rf"""{NAME} {__version__}
Copyright (C) {datetime.now().year}
Written by Wu Zhenyu
"""
EPILOG = """
Report bugs to <wuzhenyu@ustc.edu>.
"""


def get_parser() -> ArgumentParser:
    r"""Get a parser for unit test."""
    parser = ArgumentParser(
        epilog=EPILOG,
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", version=VERSION, action="version")
    parser.add_argument(
        "--print-config", help="print config value", choices=["template"]
    )
    with suppress(ImportError):
        import shtab

        shtab.add_argument_to(parser)
    return parser


def main() -> None:
    r"""Parse arguments and provide shell completions."""
    parser = get_parser()
    args = parser.parse_args()
    if args.print_config == "template":
        print(PATH)
        return None

    from .server import AutoconfLanguageServer

    AutoconfLanguageServer(NAME, __version__).start_io()


if __name__ == "__main__":
    main()
