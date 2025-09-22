from __future__ import annotations

from typing import Mapping

from _typeshed import Incomplete
from invenio_records_resources.services.records.config import SearchOptions
from invenio_records_resources.services.records.params.base import ParamInterpreter

class FacetsParam(ParamInterpreter):
    selected_values: dict[str, Incomplete]
    _filters: dict[str, Incomplete]

    def __init__(self, config: type[SearchOptions]) -> None: ...
    def add_filter(self, name: str, values: list[Incomplete]) -> None: ...
    def aggregate(self, search: Incomplete) -> Incomplete: ...
    def apply(
        self,
        identity: Incomplete,
        search: Incomplete,
        params: Mapping[str, Incomplete],
    ) -> Incomplete: ...
    @property
    def facets(self) -> dict[str, Incomplete]: ...
    def filter(self, search: Incomplete) -> Incomplete: ...
