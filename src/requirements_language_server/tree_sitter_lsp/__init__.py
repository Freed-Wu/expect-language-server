r"""Tree-sitter LSP
===================
"""
import os
from copy import deepcopy
from typing import Any
from urllib.parse import unquote, urlparse

from jinja2 import Template
from lsprotocol.types import (
    Diagnostic,
    DiagnosticSeverity,
    DocumentLink,
    Location,
    Position,
    Range,
    TextEdit,
)
from tree_sitter import Node, Tree, TreeCursor


class UNI:
    r"""Unified node identifier."""

    def __init__(self, uri: str, node: Node) -> None:
        r"""Init.

        :param uri:
        :type uri: str
        :param node:
        :type node: Node
        :rtype: None
        """
        self.uri = uri
        self.node = node

    def __repr__(self) -> str:
        r"""Repr.

        :rtype: str
        """
        return f"{self.get_text()}@{self.uri}:{self.node.start_point[0] + 1}:{self.node.start_point[1] + 1}-{self.node.end_point[0] + 1}:{self.node.end_point[1]}"

    def __eq__(self, that: "UNI") -> bool:
        r"""Eq.

        :param that:
        :type that: UNI
        :rtype: bool
        """
        return self.node == that.node

    def get_text(self) -> str:
        r"""Get text.

        :rtype: str
        """
        return self.node2text(self.node)

    @staticmethod
    def node2text(node: Node) -> str:
        r"""Node2text.

        :param node:
        :type node: Node
        :rtype: str
        """
        return node.text.decode()

    def get_location(self) -> Location:
        r"""Get location.

        :rtype: Location
        """
        return Location(self.uri, self.get_range())

    def get_range(self) -> Range:
        r"""Get range.

        :rtype: Range
        """
        return self.node2range(self.node)

    @staticmethod
    def node2range(node: Node) -> Range:
        r"""Node2range.

        :param node:
        :type node: Node
        :rtype: Range
        """
        return Range(Position(*node.start_point), Position(*node.end_point))

    def get_path(self) -> str:
        r"""Get path.

        :rtype: str
        """
        return self.uri2path(self.uri)

    @staticmethod
    def uri2path(uri: str) -> str:
        r"""Uri2path.

        :param uri:
        :type uri: str
        :rtype: str
        """
        return unquote(urlparse(uri).path)

    def get_diagnostic(
        self,
        message: str,
        severity: DiagnosticSeverity,
        **kwargs: Any,
    ) -> Diagnostic:
        r"""Get diagnostic.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        :param kwargs:
        :type kwargs: Any
        :rtype: Diagnostic
        """
        _range = self.get_range()
        _range.end.character -= 1
        return Diagnostic(
            _range,
            Template(message).render(uni=self, **kwargs),
            severity,
        )

    def get_text_edit(self, new_text: str) -> TextEdit:
        r"""Get text edit.

        :param new_text:
        :type new_text: str
        :rtype: TextEdit
        """
        return TextEdit(self.get_range(), new_text)

    def get_document_link(self, target: str, **kwargs) -> DocumentLink:
        r"""Get document link.

        :param target:
        :type target: str
        :param kwargs:
        :rtype: DocumentLink
        """
        return DocumentLink(
            self.get_range(),
            Template(target).render(uni=self, **kwargs),
        )

    @staticmethod
    def join(path, text) -> str:
        r"""Join.

        :param path:
        :param text:
        :rtype: str
        """
        return os.path.join(os.path.dirname(path), text)


class Finder:
    r"""Finder."""

    def __init__(
        self,
        message: str = "",
        severity: DiagnosticSeverity = DiagnosticSeverity.Error,
    ) -> None:
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        :rtype: None
        """
        self.level = 0
        self.message = message
        self.severity = severity
        self.reset()

    def __call__(self, uni: UNI) -> bool:
        r"""Call.

        :param uni:
        :type uni: UNI
        :rtype: bool
        """
        return True

    def __and__(self, second: "Finder") -> "Finder":
        r"""And.

        :param second:
        :type second: Finder
        :rtype: "Finder"
        """
        finder = deepcopy(self)
        finder.__call__ = lambda uni: self(uni) and second(uni)
        return finder

    def __or__(self, second: "Finder") -> "Finder":
        r"""Or.

        :param second:
        :type second: Finder
        :rtype: "Finder"
        """
        finder = deepcopy(self)
        finder.__call__ = lambda uni: self(uni) or second(uni)
        return finder

    def __minus__(self, second: "Finder") -> "Finder":
        r"""Minus.

        :param second:
        :type second: Finder
        :rtype: "Finder"
        """
        finder = deepcopy(self)
        finder.__call__ = lambda uni: self(uni) and not second(uni)
        return finder

    def is_include_node(self, node: Node) -> bool:
        r"""Is include node.

        :param node:
        :type node: Node
        :rtype: bool
        """
        return False

    def parse(self, code: bytes) -> Tree:
        r"""Parse.

        :param code:
        :type code: bytes
        :rtype: Tree
        """
        raise NotImplementedError

    def uri2tree(self, uri: str) -> Tree:
        r"""Uri2tree.

        :param uri:
        :type uri: str
        :rtype: Tree
        """
        with open(UNI.uri2path(uri), "b") as f:
            code = f.read()
        return self.parse(code)

    def node2uri(self, node: Node) -> str:
        r"""Node2uri.

        :param node:
        :type node: Node
        :rtype: str
        """
        return UNI.node2text(node)

    def move_cursor(
        self, uri: str, cursor: TreeCursor, is_all: bool = False
    ) -> str:
        r"""Move cursor.

        :param uri:
        :type uri: str
        :param cursor:
        :type cursor: TreeCursor
        :param is_all:
        :type is_all: bool
        :rtype: str
        """
        while self(UNI(uri, cursor.node)) is False:
            if self.is_include_node(cursor.node):
                self.level += 1
                old_uri = uri
                uri = self.node2uri(cursor.node)
                tree = self.uri2tree(uri)
                if is_all:
                    self.find_all(uri, tree)
                else:
                    self.find(uri, tree)
                uri = old_uri
                self.level -= 1
            if cursor.node.child_count > 0:
                cursor.goto_first_child()
                continue
            while cursor.node.next_sibling is None:
                cursor.goto_parent()
                # when cannot find new nodes, return
                if cursor.node.parent is None:
                    return ""
            cursor.goto_next_sibling()
        return uri

    def reset(self) -> None:
        r"""Reset.

        :rtype: None
        """
        pass

    def find(self, uri: str, tree: Tree | None = None) -> UNI | None:
        r"""Find.

        :param uri:
        :type uri: str
        :param tree:
        :type tree: Tree | None
        :rtype: UNI | None
        """
        self.reset()
        if tree is None:
            tree = self.uri2tree(uri)
        cursor = tree.walk()
        if uri := self.move_cursor(uri, cursor, False):
            return UNI(uri, cursor.node)
        else:
            return None

    def find_all(self, uri: str, tree: Tree | None = None) -> list[UNI]:
        r"""Find all.

        :param uri:
        :type uri: str
        :param tree:
        :type tree: Tree | None
        :rtype: list[UNI]
        """
        self.reset()
        if tree is None:
            tree = self.uri2tree(uri)
        cursor = tree.walk()
        unis = []
        while True:
            if uri := self.move_cursor(uri, cursor, True):
                unis += [UNI(uri, cursor.node)]
            while cursor.node.next_sibling is None:
                cursor.goto_parent()
                # when cannot find new nodes, return
                if cursor.node.parent is None:
                    return unis
            cursor.goto_next_sibling()

    def uni2diagnostic(self, uni: UNI) -> Diagnostic:
        r"""Uni2diagnostic.

        :param uni:
        :type uni: UNI
        :rtype: Diagnostic
        """
        return uni.get_diagnostic(self.message, self.severity)

    def unis2diagnostics(self, unis: list[UNI]) -> list[Diagnostic]:
        r"""Unis2diagnostics.

        :param unis:
        :type unis: list[UNI]
        :rtype: list[Diagnostic]
        """
        return [self.uni2diagnostic(uni) for uni in unis]
