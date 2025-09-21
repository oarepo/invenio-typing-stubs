from io import BufferedReader, BytesIO
from typing import Any, Dict, Optional, Union

from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from invenio_records_resources.services.files.transfer.providers.remote import (
    RemoteTransferBase,
)
from werkzeug.wsgi import LimitedStream

class FetchTransfer(RemoteTransferBase):
    def commit_file(self): ...
    def init_file(
        self, record: Record, file_metadata: Dict[str, Any], **kwargs
    ) -> FileRecord: ...
    def set_file_content(
        self,
        stream: Union[BytesIO, BufferedReader, LimitedStream],
        content_length: Optional[int],
    ): ...
    @property
    def status(self) -> str: ...

    class Schema(RemoteTransferBase.Schema):
        def validate_names(self, value: str): ...
