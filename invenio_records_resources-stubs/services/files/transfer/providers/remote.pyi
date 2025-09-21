from typing import Any, Dict

from flask.wrappers import Response
from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from invenio_records_resources.services.files.transfer.base import Transfer

class RemoteTransferBase(Transfer):
    class Schema:
        def validate_names(self, value: str): ...

class RemoteTransfer(RemoteTransferBase):
    def init_file(
        self, record: Record, file_metadata: Dict[str, Any], **kwargs
    ) -> FileRecord: ...
    def send_file(self, *, as_attachment, **kwargs) -> Response: ...
    @property
    def status(self) -> str: ...
