from __future__ import annotations

from functools import partial
from typing import Optional

from _typeshed import Incomplete
from invenio_records_resources.services.records.queryparser.query import QueryParser

class SuggestQueryParser(QueryParser):
    def __init__(
        self,
        identity: Optional[Incomplete] = ...,
        extra_params: Optional[dict[str, Incomplete]] = ...,
        **kwargs,
    ): ...
    def parse(self, query_str: str) -> Incomplete: ...

class CompositeSuggestQueryParser(QueryParser):
    def __init__(
        self,
        identity: Optional[Incomplete] = None,
        extra_params: Optional[dict[str, Incomplete]] = None,
        clauses: Optional[list[dict[str, Incomplete]]] = None,
        **kwargs: Incomplete,
    ): ...
    @classmethod
    def factory(
        cls,
        tree_transformer_cls: Optional[type] = ...,
        clauses: Optional[list[dict[str, Incomplete]]] = ...,
        filter_field: Optional[str] = ...,
        **extra_params,
    ) -> partial: ...
    def extract_subtypes(self, query_str: str) -> tuple[Incomplete, str]: ...
