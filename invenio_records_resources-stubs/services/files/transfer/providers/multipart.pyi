from io import BytesIO
from typing import (
    Any,
    Dict,
    Union,
)

from flask_principal import (
    Identity,
)
from invenio_files_rest.storage.base import FileStorage
from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from werkzeug.wsgi import LimitedStream

class MultipartStorageExt:
    def __getattr__(self, name: str) -> str: ...
    def __init__(self, storage: FileStorage): ...
    def multipart_commit_upload(self, **multipart_metadata) -> str: ...
    def multipart_initialize_upload(
        self, parts: int, size: int, part_size: int
    ) -> Dict[str, str]: ...
    def multipart_links(
        self, base_url: str, **multipart_metadata
    ) -> Dict[str, Any]: ...
    def multipart_set_content(
        self,
        part: int,
        stream: Union[BytesIO, LimitedStream],
        content_length: int,
        **multipart_metadata,
    ) -> Dict[Any, Any]: ...

class MultipartTransfer:
    def _get_storage(self, **kwargs) -> MultipartStorageExt: ...
    def commit_file(self): ...
    def expand_links(self, identity: Identity, self_url: str) -> Dict[str, Any]: ...
    def init_file(
        self,
        record: Record,
        file_metadata: Dict[str, Any],
        **kwargs,
    ) -> FileRecord: ...
    @property
    def multipart_metadata(self) -> Dict[str, Union[str, int]]: ...
    def set_file_multipart_content(
        self, part: int, stream: Union[BytesIO, LimitedStream], content_length: int
    ): ...
    @property
    def status(self) -> str: ...
