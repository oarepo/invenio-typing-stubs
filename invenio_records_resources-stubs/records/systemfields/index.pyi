from typing import Optional, Union

from invenio_records.systemfields.base import SystemField
from invenio_records_resources.records.api import Record
from opensearch_dsl.index import Index  # type: ignore[import-untyped]

class IndexField[R: Record = Record](SystemField[R, Index]):
    _index: Index

    def __init__(
        self, index_or_alias: Union[Index, str], search_alias: Optional[str] = ...
    ) -> None: ...
