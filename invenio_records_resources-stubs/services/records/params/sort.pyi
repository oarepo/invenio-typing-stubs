from typing import Any, Dict, List

from flask_principal import (
    Identity,
)
from invenio_search.api import RecordsSearchV2

class SortParam:
    def _compute_sort_fields(self, params: Dict[str, Any]) -> List[str]: ...
    def _default_sort(
        self,
        params: Dict[str, Any],
        options: Dict[str, Any],
    ) -> str: ...
    def _handle_empty_query(
        self,
        params: Dict[str, Any],
        options: Dict[str, Any],
    ) -> str: ...
    def apply(
        self,
        identity: Identity,
        search: RecordsSearchV2,
        params: Dict[str, Any],
    ) -> RecordsSearchV2: ...
