from io import (
    BufferedReader,
    BytesIO,
)
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Type,
    Union,
)
from uuid import UUID

from invenio_files_rest.models import (
    Bucket,
    ObjectVersion,
)
from invenio_records_resources.records.api import FileRecord, Record
from werkzeug.wsgi import LimitedStream

def ensure_enabled(func: Callable) -> Callable: ...

class FilesManager[R: Record = Record, F: FileRecord = FileRecord]:
    def __getitem__(self, key: str) -> F: ...
    def __init__(
        self,
        record: R,
        file_cls: Optional[Type[F]] = ...,
        bucket: None = ...,
        enabled: bool = ...,
        order: None = ...,
        default_preview: Optional[str] = ...,
        entries: None = ...,
        options: Optional[Dict[str, str]] = ...,
    ): ...
    def __len__(self) -> int: ...
    def __setitem__(self, key: str, value: Any): ...
    def _parse_set_value(self, value: Any) -> Any: ...
    @property
    def bucket(self) -> Bucket: ...
    @property
    def bucket_id(self) -> UUID: ...
    def commit(self, file_key: str): ...
    def copy(self, src_files: FilesManager, copy_obj: bool = ...): ...
    @property
    def count(self) -> int: ...
    def create(
        self, key: str, *, obj=..., stream=..., data=..., transfer=..., **kwargs
    ) -> F: ...
    def create_bucket(self): ...
    def create_obj(
        self,
        key: str,
        stream: Union[BufferedReader, BytesIO, LimitedStream],
        data: None = ...,
        **kwargs,
    ) -> ObjectVersion: ...
    def delete(
        self,
        key: str,
        remove_obj: bool = ...,
        softdelete_obj: bool = ...,
        remove_rf: bool = ...,
    ) -> F: ...
    def delete_all(
        self, remove_obj: bool = ..., softdelete_obj: bool = ..., remove_rf: bool = ...
    ): ...
    @property
    def entries(self) -> Dict[str, F]: ...
    @property
    def exts(self) -> List[Any]: ...
    @property
    def mimetypes(self) -> List[Any]: ...
    def remove_bucket(self, force: bool = ...): ...
    def set_bucket(self, bucket: Bucket, overwrite: bool = ...): ...
    def sync(self, src_files: FilesManager, delete_extras: bool = ...): ...
    def teardown(self, full: bool = ...): ...
    @property
    def total_bytes(self) -> int: ...
    def unset_bucket(self): ...
    def update(
        self,
        key: str,
        obj: Optional[ObjectVersion] = ...,
        stream: Optional[BytesIO] = ...,
        data: Optional[Dict[str, Dict[str, str]]] = ...,
        **kwargs,
    ) -> F: ...
