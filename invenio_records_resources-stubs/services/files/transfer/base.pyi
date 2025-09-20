from io import (
    BufferedReader,
    BytesIO,
)
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

from flask_principal import (
    Identity,
)
from invenio_db.uow import UnitOfWork
from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from invenio_records_resources.services.files.service import FileService
from werkzeug.wsgi import LimitedStream

class Transfer:
    def __init__(
        self,
        record: Record,
        key: str,
        file_service: Optional[FileService],
        file_record: Optional[FileRecord] = ...,
        uow: Optional[UnitOfWork] = ...,
    ): ...
    def commit_file(self): ...
    def delete_file(self): ...
    def expand_links(self, identity: Identity, self_url: str) -> Dict[Any, Any]: ...
    @property
    def file_record(self) -> FileRecord: ...
    def init_file(
        self,
        record: Record,
        file_metadata: Dict[
            str,
            Union[
                Dict[str, str], str, Dict[str, Union[str, int]], int, Dict[str, bool]
            ],
        ],
        **kwargs,
    ) -> FileRecord: ...
    def send_file(self, *, restricted, as_attachment): ...
    def set_file_content(
        self,
        stream: Union[BytesIO, BufferedReader, LimitedStream],
        content_length: Optional[int],
    ): ...
    @property
    def status(self) -> str: ...
