from typing import (
    Any,
    Dict,
    Optional,
    Type,
)

from invenio_records.dumpers.search import SearchDumper
from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import FileRecord, Record
from invenio_records_resources.records.systemfields.files.manager import FilesManager

class FilesField[R: Record = Record](SystemField[R, FilesManager]):
    def __init__(
        self,
        key: str = ...,
        bucket_id_attr: str = ...,
        bucket_attr: str = ...,
        store: bool = ...,
        dump: bool = ...,
        dump_entries: bool = ...,
        file_cls: Optional[Type[FileRecord]] = ...,
        enabled: bool = ...,
        bucket_args: None = ...,
        create: bool = ...,
        delete: bool = ...,
    ): ...
    @property
    def _manager_options(self) -> Dict[str, str]: ...
    def dump(
        self, record: R, files: FilesManager, include_entries: bool = ...
    ) -> Dict[str, Any]: ...
    @property
    def file_cls(self) -> Type[FileRecord]: ...
    def load(
        self,
        record: R,
        data: Dict[str, Any],
        from_dump: bool = ...,
    ) -> FilesManager: ...
    def obj(self, record: R) -> FilesManager: ...
    def post_create(self, record: R): ...
    def post_dump(self, record: R, data: Dict[str, Any], **kwargs): ...
    def pre_commit(self, record: R): ...
    def pre_load(
        self,
        data: Dict[str, Any],
        loader: Optional[SearchDumper] = ...,
    ): ...
    def store(self, record: R, files: FilesManager): ...
