from io import BytesIO
from typing import Any, ClassVar, Dict, Union

from flask_principal import (
    Identity,
)
from invenio_files_rest.storage.base import FileStorage
from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from invenio_records_resources.services.files.schema import BaseTransferSchema
from invenio_records_resources.services.files.transfer.base import Transfer
from werkzeug.wsgi import LimitedStream

class MultipartStorageExt:
    def __getattr__(self, name: str) -> str: ...
    def __init__(self, storage: FileStorage): ...
    def multipart_commit_upload(self, **multipart_metadata) -> str | None: ...
    def multipart_initialize_upload(
        self, parts: int, size: int, part_size: int
    ) -> Dict[str, Any]: ...
    def multipart_links(
        self, base_url: str, **multipart_metadata
    ) -> Dict[str, Any]: ...
    def multipart_set_content(
        self,
        part: int,
        stream: Union[BytesIO, LimitedStream],
        content_length: int,
        **multipart_metadata,
    ) -> Dict[str, Any]: ...

class MultipartTransfer(Transfer):
    transfer_type: ClassVar[str]

    class Schema(BaseTransferSchema): ...

    def _get_storage(self, **kwargs) -> MultipartStorageExt: ...
    def commit_file(self) -> None: ...
    def expand_links(self, identity: Identity, self_url: str) -> Dict[str, Any]: ...
    def init_file(
        self,
        record: Record,
        file_metadata: Dict[str, Any],
        **kwargs,
    ) -> FileRecord: ...
    @property
    def multipart_metadata(self) -> Dict[str, Any]: ...
    def set_file_multipart_content(
        self, part: int, stream: Union[BytesIO, LimitedStream], content_length: int
    ) -> None: ...
    @property
    def status(self) -> str: ...
