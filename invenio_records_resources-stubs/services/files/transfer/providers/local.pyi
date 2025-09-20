from io import (
    BufferedReader,
    BytesIO,
)
from typing import (
    Optional,
    Union,
)
from werkzeug.wsgi import LimitedStream


class LocalTransfer:
    def set_file_content(
        self,
        stream: Union[BytesIO, BufferedReader, LimitedStream],
        content_length: Optional[int]
    ): ...
