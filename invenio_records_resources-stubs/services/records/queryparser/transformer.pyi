from __future__ import annotations

from typing import Callable, Optional

from _typeshed import Incomplete
from invenio_access.permissions import Permission  # type: ignore[import-untyped]
from luqum.tree import Phrase, SearchField, Word  # type: ignore[import-untyped]
from luqum.visitor import TreeTransformer  # type: ignore[import-untyped]

class FieldValueMapper:
    def __init__(
        self, term_name: str, word: Optional[Callable] = ..., phrase: None = ...
    ): ...
    def map_word(self, node: Word, **kwargs) -> Incomplete: ...
    def map_phrase(self, node: Phrase, **kwargs) -> Incomplete: ...
    @property
    def term_name(self) -> str: ...

class RestrictedTerm:
    def __init__(self, permission: Permission): ...
    def allows(self, identity: Incomplete) -> bool: ...

class RestrictedTermValue:
    def __init__(
        self, permission: Permission, word: Optional[Callable] = ..., phrase: None = ...
    ): ...
    def map_word(
        self,
        node: Word,
        context: dict[str, Incomplete],
        **kwargs,
    ) -> Incomplete: ...
    def map_phrase(
        self,
        node: Phrase,
        context: dict[str, Incomplete],
        **kwargs,
    ) -> Incomplete: ...

class SearchFieldTransformer(TreeTransformer):
    def __init__(
        self,
        mapping: dict[str, Incomplete],
        allow_list: set[str],
        *args,
        **kwargs,
    ): ...
    def visit_search_field(
        self,
        node: SearchField,
        context: dict[str, Incomplete],
    ): ...
    def visit_word(
        self,
        node: Word,
        context: dict[str, Incomplete],
    ): ...
    def visit_phrase(
        self,
        node: Phrase,
        context: dict[str, Incomplete],
    ): ...
