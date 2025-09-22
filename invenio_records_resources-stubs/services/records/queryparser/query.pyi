from __future__ import annotations

from functools import partial
from typing import Optional

from _typeshed import Incomplete
from invenio_records_resources.services.records.queryparser.transformer import (
    SearchFieldTransformer,
)

class QueryParser:
    def __init__(
        self,
        identity: Optional[Incomplete] = ...,
        extra_params: Optional[dict[str, Incomplete]] = ...,
        tree_transformer_cls: Optional[type[SearchFieldTransformer]] = ...,
    ): ...
    @property
    def allow_list(self) -> set[str]: ...
    @classmethod
    def factory(
        cls,
        tree_transformer_cls: Optional[type[SearchFieldTransformer]] = ...,
        **extra_params,
    ) -> partial: ...
    @property
    def fields(self) -> list[str]: ...
    def parse(self, query_str: str) -> Incomplete: ...
