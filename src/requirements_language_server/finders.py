r"""Finders
===========
"""
from lsprotocol.types import DiagnosticSeverity
from pip_cache import get_package_names

from .tree_sitter_lsp import UNI, Finder
from .tree_sitter_lsp.finders import (
    NonExistentFinder,
    RepeatedFinder,
    UnsortedFinder,
)


class InvalidPackageFinder(Finder):
    r"""Invalidpackagefinder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: no such package",
        severity: DiagnosticSeverity = DiagnosticSeverity.Error,
    ) -> None:
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        :rtype: None
        """
        super().__init__(message, severity)

    def __call__(self, uni: UNI) -> bool:
        r"""Call.

        :param uni:
        :type uni: UNI
        :rtype: bool
        """
        text = uni.get_text()
        return uni.node.type == "package" and text not in get_package_names(
            text
        )


class InvalidPathFinder(NonExistentFinder):
    r"""Invalidpathfinder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: no such package",
        severity: DiagnosticSeverity = DiagnosticSeverity.Error,
    ) -> None:
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        :rtype: None
        """
        super().__init__(message, severity)

    def __call__(self, uni: UNI) -> bool:
        r"""Call.

        :param uni:
        :type uni: UNI
        :rtype: bool
        """
        return uni.node.type == "path" and self.is_non_existent(uni)


class RepeatedPackageFinder(RepeatedFinder):
    r"""Repeatedpackagefinder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: is repeated on {{_uni}}",
        severity: DiagnosticSeverity = DiagnosticSeverity.Warning,
    ) -> None:
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        :rtype: None
        """
        super().__init__(message, severity)

    def filter(self, uni: UNI) -> bool:
        r"""Filter.

        :param uni:
        :type uni: UNI
        :rtype: bool
        """
        return uni.node.type == "package"


class UnsortedRequirementFinder(UnsortedFinder):
    r"""Unsortedrequirementfinder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: is unsorted due to {{_uni}}",
        severity: DiagnosticSeverity = DiagnosticSeverity.Warning,
    ) -> None:
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        :rtype: None
        """
        super().__init__(message, severity)

    def filter(self, uni: UNI) -> bool:
        r"""Filter.

        :param uni:
        :type uni: UNI
        :rtype: bool
        """
        return uni.node.type == "requirement"
