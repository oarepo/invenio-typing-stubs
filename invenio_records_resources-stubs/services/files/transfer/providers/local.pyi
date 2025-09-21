from io import (
    BufferedReader,
    BytesIO,
)
from typing import (
    Optional,
    Union,
)

from invenio_records_resources.services.files.transfer.base import Transfer
from werkzeug.wsgi import LimitedStream

class LocalTransfer(Transfer):
    def set_file_content(
        self,
        stream: Union[BytesIO, BufferedReader, LimitedStream],
        content_length: Optional[int],
    ): ...
