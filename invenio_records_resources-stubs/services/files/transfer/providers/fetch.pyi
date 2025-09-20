from io import BytesIO
from typing import Any, Dict, Optional

from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)

class FetchTransfer:
    def commit_file(self): ...
    def init_file(
        self, record: Record, file_metadata: Dict[str, Any], **kwargs
    ) -> FileRecord: ...
    def set_file_content(self, stream: BytesIO, content_length: Optional[int]): ...
    @property
    def status(self) -> str: ...

    class Schema:
        def validate_names(self, value: str): ...
