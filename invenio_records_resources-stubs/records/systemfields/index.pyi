from typing import Optional, Union

from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import Record
from invenio_search.engine import dsl

class IndexField[R: Record = Record](SystemField[R, dsl.Index]):
    _index: dsl.Index

    def __init__(
        self, index_or_alias: Union[dsl.Index, str], search_alias: Optional[str] = ...
    ) -> None: ...
