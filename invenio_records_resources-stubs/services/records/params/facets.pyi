from typing import Any, Dict, List, Type

from flask_principal import (
    Identity,
)
from invenio_records_resources.services.records.config import SearchOptions
from invenio_records_resources.services.records.facets.facets import TermsFacet
from invenio_search.api import RecordsSearchV2  # type: ignore[import-untyped]

class FacetsParam:
    def __init__(self, config: Type[SearchOptions]): ...
    def add_filter(self, name: str, values: List[str]): ...
    def aggregate(self, search: RecordsSearchV2) -> RecordsSearchV2: ...
    def apply(
        self,
        identity: Identity,
        search: RecordsSearchV2,
        params: Dict[str, Any],
    ) -> RecordsSearchV2: ...
    @property
    def facets(self) -> Dict[str, TermsFacet]: ...
    def filter(self, search: RecordsSearchV2) -> RecordsSearchV2: ...
