from typing import Any, Callable, Dict, Optional, Set

from invenio_access.permissions import Permission
from luqum.tree import (  # type: ignore[import-untyped]
    SearchField,
    Word,
)

class FieldValueMapper:
    def __init__(
        self, term_name: str, word: Optional[Callable] = ..., phrase: None = ...
    ): ...
    def map_word(self, node: Word, **kwargs) -> Any: ...
    @property
    def term_name(self) -> str: ...

class RestrictedTerm:
    def __init__(self, permission: Permission): ...

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
