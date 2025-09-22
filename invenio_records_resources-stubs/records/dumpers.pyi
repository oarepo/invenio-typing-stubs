from typing import Any, Dict, Type

from invenio_records.dumpers import Dumper, SearchDumperExt
from invenio_records_resources.records.api import FileRecord

class CustomFieldsDumperExt(SearchDumperExt):
    _fields_var: str
    key: str

    def __init__(self, fields_var: str, key: str = ...) -> None: ...
    def dump(self, record: Any, data: Dict[str, Any]) -> None: ...
    def load(self, data: Dict[str, Any], record_cls: Type[Any]) -> None: ...

class PartialFileDumper(Dumper):
    def dump(self, record: Any, data: Any = ...) -> Dict[str, Any]: ...
    def load(
        self,
        data: Dict[str, Any],
        record_cls: Type[FileRecord],
    ) -> FileRecord: ...
