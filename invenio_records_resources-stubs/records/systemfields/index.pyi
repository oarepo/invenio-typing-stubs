from typing import (
    Optional,
)

from invenio_records.systemfields.base import SystemField
from invenio_records_resources.records.api import (
    Record,
)
from opensearch_dsl.index import Index

class IndexField[R: Record = Record](SystemField[R, Index]):
    def __init__(self, index_or_alias: str, search_alias: Optional[str] = ...): ...
