from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Type,
)

from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import FileRecord, Record

# type: ignore[import-untyped]
from invenio_records_resources.records.systemfields.files.manager import FilesManager

class FilesField[R: Record = Record](SystemField[R, FilesManager]):
    def __init__(
        self,
        key: str = ...,
        bucket_id_attr: str = ...,
        bucket_attr: str = ...,
        store: bool = ...,
        dump: bool = ...,
        dump_entries: Any = ...,
        file_cls: Optional[Type[FileRecord]] = ...,
        enabled: bool = ...,
        bucket_args: Optional[Dict[str, Any] | Callable[..., Dict[str, Any]]] = ...,
        create: bool = ...,
        delete: bool = ...,
    ): ...
    @property
    def _manager_options(self) -> Dict[str, Any]: ...
    def dump(
        self, record: R, files: FilesManager, include_entries: bool = ...
    ) -> Dict[str, Any]: ...
    @property
    def file_cls(self) -> Optional[Type[FileRecord]]: ...
    def load(
        self,
        record: R,
        data: Dict[str, Any],
        from_dump: bool = ...,
    ) -> FilesManager: ...
    def obj(self, record: R) -> Optional[FilesManager]: ...
    def store(self, record: R, files: FilesManager): ...
