from contextlib import contextmanager
from typing import Any, Dict, Iterator, Optional, Self, Type
from uuid import UUID

from invenio_files_rest.models import (
    FileInstance,
    ObjectVersion,
)
from invenio_records.api import Record as RecordBase
from invenio_records.systemfields import SystemFieldsMixin

class Record(RecordBase, SystemFieldsMixin):
    send_signals: bool
    enable_jsonref: bool
    model_cls: Optional[Type[Any]]
    dumper: Any
    metadata: Any

class File:
    object_model: Optional[ObjectVersion]
    file_model: Optional[FileInstance]

    def __getattr__(self, name: str) -> Any: ...
    def __init__(
        self,
        object_model: Optional[ObjectVersion] = ...,
        file_model: Optional[FileInstance] = ...,
    ): ...
    def dumps(self) -> Dict[str, Any]: ...
    @property
    def ext(self) -> str: ...
    @classmethod
    def from_dump(cls, data: Dict[str, Any]) -> Self: ...
    @property
    def key(self) -> str: ...
    @property
    def file_id(self) -> UUID: ...

class FileAccess:
    dirty: bool

    def __init__(self, hidden: Optional[bool] = ...): ...
    def dump(self) -> Dict[str, bool]: ...
    @classmethod
    def from_dict(cls, access_dict: Dict[str, bool]) -> Self: ...
    @property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, value: bool) -> None: ...

class FileAccessField:
    def __get__(
        self, record: Optional[FileRecord], owner: Optional[Type[FileRecord]] = ...
    ) -> FileAccess: ...
    def __init__(
        self, key: Optional[str] = ..., access_obj_class: Type[FileAccess] = ...
    ): ...
    def __set__(self, record: FileRecord, obj: Any) -> None: ...
    def obj(self, instance: FileRecord) -> FileAccess: ...
    def set_obj(self, record: FileRecord, obj: Any) -> None: ...
    def pre_commit(self, record: FileRecord) -> None: ...

class FileRecord(RecordBase, SystemFieldsMixin):
    send_signals: bool
    enable_jsonref: bool
    model_cls: Optional[Type[Any]]
    record_cls: Optional[Type[Any]]
    dumper: Any
    metadata: Any
    access: FileAccess
    key: Any
    object_version_id: Any
    object_version: Any
    record_id: Any
    _record: Any
    transfer: Any

    @property
    def file(self) -> Optional[File]: ...
    @classmethod
    def get_by_key(cls, record_id: UUID, key: str) -> Optional[Self]: ...
    def get_stream(self, mode: str) -> Any: ...
    @classmethod
    def list_by_record(
        cls, record_id: UUID, with_deleted: bool = ...
    ) -> Iterator[Self]: ...
    @contextmanager
    def open_stream(self, mode: str) -> Iterator[Any]: ...
    @property
    def record(self) -> Any: ...
    @classmethod
    def remove_all(cls, record_id: UUID) -> None: ...

class PersistentIdentifierWrapper:
    pid_value: str

    def __init__(self, pid_value: str) -> None: ...
