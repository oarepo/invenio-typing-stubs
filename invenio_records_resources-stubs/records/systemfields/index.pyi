from typing import Any, Optional

from invenio_records.systemfields.base import SystemField
from invenio_records_resources.records.api import (
    Record,
)
from opensearch_dsl.index import Index  # type: ignore[import-untyped]

class IndexField[R: Record = Record](SystemField[R, Index]):
    def __init__(self, index_or_alias: Any, search_alias: Optional[str] = ...): ...
