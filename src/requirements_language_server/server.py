r"""Server
==========
"""
import os
import re
from typing import Any, Tuple

from jinja2 import Template
from lsprotocol.types import (
    INITIALIZE,
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    Hover,
    InitializeParams,
    MarkupContent,
    MarkupKind,
    Position,
    Range,
    TextDocumentPositionParams,
)
from pip._internal.commands.show import search_packages_info
from pip_cache import get_package_names
from pygls.server import LanguageServer

from . import PATH

NOT_FOUND = "Not found installed package!"
if not os.path.exists(PATH):
    PATH = os.path.join(
        os.path.join(
            os.path.join(os.path.dirname(__file__), "assets"), "jinja2"
        ),
        "template.md.j2",
    )
with open(PATH, "r") as f:
    TEMPLATE = f.read()


def get_document(pkgname: str, template: str) -> str:
    r"""Get document.

    :param pkgname:
    :type pkgname: str
    :param template:
    :type template: str
    :rtype: str
    """
    try:
        info = list(search_packages_info([pkgname]))[0]
        output = Template(template).render(info=info)
    except IndexError:
        output = NOT_FOUND
    return output


class AutoconfLanguageServer(LanguageServer):
    r"""Autoconflanguageserver."""

    def __init__(self, *args: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :rtype: None
        """
        super().__init__(*args)
        self.template = ""

        @self.feature(INITIALIZE)
        def initialize(params: InitializeParams) -> None:
            r"""Initialize.

            :param params:
            :type params: InitializeParams
            :rtype: None
            """
            opts = params.initialization_options
            self.template = getattr(opts, "template", TEMPLATE)

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            word = self._cursor_word(
                params.text_document.uri, params.position, True
            )
            if not word or word[0].startswith("-"):
                return None
            doc = get_document(word[0], self.template)
            if not doc:
                return None
            return Hover(
                contents=MarkupContent(kind=MarkupKind.Markdown, value=doc),
                range=word[1],
            )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            word = self._cursor_word(
                params.text_document.uri, params.position, False
            )
            token = "" if word is None else word[0]
            if token.startswith("-"):
                items = [
                    CompletionItem(
                        label=x,
                        kind=CompletionItemKind.Function,
                        documentation="pip option",
                        insert_text=x,
                    )
                    for x in get_package_names(token)
                ]
            else:
                items = [
                    CompletionItem(
                        label=x,
                        kind=CompletionItemKind.Function,
                        documentation=get_document(x, TEMPLATE),
                        insert_text=x,
                    )
                    for x in get_package_names(token)
                ]
            return CompletionList(is_incomplete=False, items=items)

    def _cursor_line(self, uri: str, position: Position) -> str:
        r"""Cursor line.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :rtype: str
        """
        doc = self.workspace.get_document(uri)
        content = doc.source
        line = content.split("\n")[position.line]
        return str(line)

    def _cursor_word(
        self, uri: str, position: Position, include_all: bool = True
    ) -> Tuple[str, Range] | None:
        r"""Cursor word.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :param include_all:
        :type include_all: bool
        :rtype: Tuple[str, Range] | None
        """
        line = self._cursor_line(uri, position)
        cursor = position.character
        for m in re.finditer(r"\w+", line):
            end = m.end() if include_all else cursor
            if m.start() <= cursor <= m.end():
                word = (
                    line[m.start() : end],
                    Range(
                        start=Position(
                            line=position.line, character=m.start()
                        ),
                        end=Position(line=position.line, character=end),
                    ),
                )
                return word
        return None
