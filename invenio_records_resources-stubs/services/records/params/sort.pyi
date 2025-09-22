from __future__ import annotations

from typing import Mapping

from _typeshed import Incomplete
from invenio_records_resources.services.records.params.base import ParamInterpreter

class SortParam(ParamInterpreter):
    def _compute_sort_fields(self, params: Mapping[str, Incomplete]) -> list[str]: ...
    def _default_sort(
        self,
        params: Mapping[str, Incomplete],
        options: Mapping[str, Incomplete],
    ) -> str: ...
    def _handle_empty_query(
        self,
        params: Mapping[str, Incomplete],
        options: Mapping[str, Incomplete],
    ) -> str: ...
    def apply(
        self,
        identity: Incomplete,
        search: Incomplete,
        params: Mapping[str, Incomplete],
    ) -> Incomplete: ...
