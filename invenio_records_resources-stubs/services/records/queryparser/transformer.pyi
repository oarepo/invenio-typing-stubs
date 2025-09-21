from typing import Any, Callable, Dict, Optional, Set

from flask_principal import Identity
from invenio_access.permissions import Permission  # type: ignore[import-untyped]
from luqum.tree import (  # type: ignore[import-untyped]
    Phrase,
    SearchField,
    Word,
)

class FieldValueMapper:
    def __init__(
        self, term_name: str, word: Optional[Callable] = ..., phrase: None = ...
    ): ...
    def map_word(self, node: Word, **kwargs) -> Any: ...
    def map_phrase(self, node: Phrase, **kwargs) -> Any: ...
    @property
    def term_name(self) -> str: ...

class RestrictedTerm:
    def __init__(self, permission: Permission): ...
    def allows(self, identity: Identity) -> bool: ...

class RestrictedTermValue:
    def __init__(
        self, permission: Permission, word: Optional[Callable] = ..., phrase: None = ...
    ): ...
    def map_word(
        self,
        node: Word,
        context: Dict[str, Any],
        **kwargs,
    ) -> Word: ...
    def map_phrase(
        self,
        node: Phrase,
        context: Dict[str, Any],
        **kwargs,
    ) -> Phrase: ...

class SearchFieldTransformer:
    def __init__(
        self,
        mapping: Dict[str, Any],
        allow_list: Set[str],
        *args,
        **kwargs,
    ): ...
    def visit_search_field(
        self,
        node: SearchField,
        context: Dict[str, Any],
    ): ...
    def visit_word(
        self,
        node: Word,
        context: Dict[str, Any],
    ): ...
    def visit_phrase(
        self,
        node: Phrase,
        context: Dict[str, Any],
    ): ...
