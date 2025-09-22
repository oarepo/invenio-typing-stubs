from contextlib import contextmanager
from typing import Any, ClassVar, Dict, Generator, Optional, Self, Type
from uuid import UUID

from invenio_files_rest.models import (  # type: ignore[import-untyped]
    FileInstance,
    ObjectVersion,
)
from invenio_records.api import Record as RecordBase
from invenio_records.systemfields import SystemField, SystemFieldsMixin
from invenio_records_resources.records.systemfields import PIDField

class Record(RecordBase, SystemFieldsMixin):
    send_signals: ClassVar[bool]
    enable_jsonref: ClassVar[bool]
    model_cls: ClassVar[Optional[Type[Any]]]
    dumper: ClassVar[Any]
    metadata: ClassVar[Any]
    pid: ClassVar[
        PIDField
    ]  # keep typing ; this is not present on the record but is used overall

class FileAccess:
    _hidden: bool
    dirty: bool

    def __init__(self, hidden: Optional[bool] = ...) -> None: ...
    def dump(self) -> Dict[str, bool]: ...
    @classmethod
    def from_dict(cls, access_dict: Dict[str, bool]) -> Self: ...
    @property
    def hidden(self) -> bool: ...
    @hidden.setter
    def hidden(self, value: bool) -> None: ...

class FileAccessField(SystemField[FileRecord, FileAccess]):
    _access_obj_class: Type[FileAccess]

    def __init__(
        self, key: Optional[str] = ..., access_obj_class: Type[FileAccess] = ...
    ) -> None: ...
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
    ) -> Generator[Self, None, None]: ...
    @contextmanager
    def open_stream(self, mode: str) -> Generator[Any, None, None]: ...
    @property
    def record(self) -> Any: ...
    @classmethod
    def remove_all(cls, record_id: UUID) -> None: ...

class File:
    object_model: Optional[ObjectVersion]
    file_model: Optional[FileInstance]

    def __getattr__(self, name: str) -> Any: ...
    def __init__(
        self,
        object_model: Optional[ObjectVersion] = ...,
        file_model: Optional[FileInstance] = ...,
    ) -> None: ...
    def dumps(self) -> Dict[str, Any]: ...
    @property
    def ext(self) -> Optional[str]: ...
    @classmethod
    def from_dump(cls, data: Dict[str, Any]) -> Self: ...
    @property
    def key(self) -> str: ...
    @property
    def file_id(self) -> UUID: ...

class PersistentIdentifierWrapper:
    pid_value: str

    def __init__(self, pid_value: str) -> None: ...
