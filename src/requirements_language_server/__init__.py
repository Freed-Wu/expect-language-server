r"""Provide ``__version__`` for
`importlib.metadata.version() <https://docs.python.org/3/library/importlib.metadata.html#distribution-versions>`_.
"""
import os

from platformdirs import user_config_dir

from ._version import __version__, __version_tuple__  # type: ignore

__all__ = ["__version__", "__version_tuple__"]

PATH = os.path.join(user_config_dir("requirements"), "template.j2")
