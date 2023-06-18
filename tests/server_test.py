r"""Test api"""
from requirements_language_server.server import (
    NOT_FOUND,
    TEMPLATE,
    get_document,
)


class Test:
    r"""Test."""

    @staticmethod
    def test_get_document() -> None:
        r"""Test get document.

        :rtype: None
        """
        assert get_document("pip", TEMPLATE) != NOT_FOUND
