r"""Server
==========
"""
import json
import os
import re
from typing import Any, Literal, Tuple

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
from platformdirs import user_cache_dir
from pygls.server import LanguageServer


def get_document(
    method: Literal["builtin", "cache", "system"] = "builtin"
) -> dict[str, str]:
    r"""Get document. ``builtin`` will use builtin expect.json. ``cache``
    will generate a cache from ``${XDG_CACHE_DIRS:-/usr/share}
    /man/man5/neoexpectrc.5.gz``. ``system`` is same as ``cache`` except it
    doesn't generate cache. We use ``builtin`` as default.

    :param method:
    :type method: Literal["builtin", "cache", "system"]
    :rtype: dict[str, str]
    """
    if method == "builtin":
        file = os.path.join(
            os.path.join(
                os.path.join(os.path.dirname(__file__), "assets"), "json"
            ),
            "expect.json",
        )
        with open(file, "r") as f:
            document = json.load(f)
    elif method == "cache":
        from .api import init_document

        if not os.path.exists(user_cache_dir("expect.json")):
            document = init_document()
            with open(user_cache_dir("expect.json"), "w") as f:
                json.dump(document, f)
        else:
            with open(user_cache_dir("expect.json"), "r") as f:
                document = json.load(f)
    else:
        from .api import init_document

        document = init_document()
    return document


class ExpectLanguageServer(LanguageServer):
    r"""Expect language server."""

    def __init__(self, *args: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :rtype: None
        """
        super().__init__(*args)
        self.document = {}

        @self.feature(INITIALIZE)
        def initialize(params: InitializeParams) -> None:
            r"""Initialize.

            :param params:
            :type params: InitializeParams
            :rtype: None
            """
            opts = params.initialization_options
            method = getattr(opts, "method", "builtin")
            self.document = get_document(method)  # type: ignore

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
            if not word:
                return None
            result = self.document.get(word[0])
            if not result:
                return None
            return Hover(
                contents=MarkupContent(kind=MarkupKind.Markdown, value=result),
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
            items = [
                CompletionItem(
                    label=x,
                    kind=CompletionItemKind.Function,
                    documentation=MarkupContent(
                        kind=MarkupKind.Markdown, value=self.document[x]
                    ),
                    insert_text=x,
                )
                for x in self.document
                if x.startswith(token)
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
        self,
        uri: str,
        position: Position,
        include_all: bool = True,
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
        pat = r"[a-z_-]+"
        line = self._cursor_line(uri, position)
        cursor = position.character
        for m in re.finditer(pat, line):
            end = m.end() if include_all else cursor
            if m.start() <= cursor <= m.end():
                word = (
                    line[m.start() : end],
                    Range(
                        Position(position.line, m.start()),
                        Position(position.line, end),
                    ),
                )
                return word
        return None
