from typing import (
    Any,
    Dict,
    Type,
)

from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)

class CustomFieldsDumperExt:
    def __init__(self, fields_var: str, key: str = ...): ...
    def dump(self, record: None, data: Record): ...
    def load(self, data: Record, record_cls: None): ...

class PartialFileDumper:
    def dump(self, record: FileRecord, data: Dict[Any, Any]) -> Dict[str, Any]: ...
    def load(
        self,
        data: Dict[str, Any],
        record_cls: Type[FileRecord],
    ) -> FileRecord: ...
