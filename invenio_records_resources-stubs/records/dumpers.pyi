from _typeshed import Incomplete
from invenio_records.api import Record as BaseRecord
from invenio_records.dumpers import Dumper, SearchDumperExt
from invenio_records_resources.records.api import FileRecord

class CustomFieldsDumperExt(SearchDumperExt):
    _fields_var: str
    key: str

    def __init__(self, fields_var: str, key: str = ...) -> None: ...
    def dump(self, record: BaseRecord, data: dict[str, Incomplete]) -> None: ...
    def load(
        self, data: dict[str, Incomplete], record_cls: type[BaseRecord]
    ) -> None: ...

class PartialFileDumper(Dumper):
    def dump(
        self, record: BaseRecord, data: dict[str, Incomplete] = ...
    ) -> dict[str, Incomplete]: ...
    def load(
        self,
        data: dict[str, Incomplete],
        record_cls: type[BaseRecord],
    ) -> FileRecord: ...
