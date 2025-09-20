from collections.abc import Generator
from typing import Any

from invenio_vocabularies.datastreams.errors import ReaderError as ReaderError
from invenio_vocabularies.datastreams.readers import BaseReader as BaseReader

class OpenAIREHTTPReader(BaseReader):
    tar_href: str | None
    def __init__(
        self, origin=None, mode: str = "r", tar_href=None, *args, **kwargs
    ) -> None: ...
    def read(self, item=None, *args, **kwargs) -> Generator[Any]: ...

VOCABULARIES_DATASTREAM_READERS: dict[str, type[OpenAIREHTTPReader]]
VOCABULARIES_DATASTREAM_TRANSFORMERS: dict[str, Any]
VOCABULARIES_DATASTREAM_WRITERS: dict[str, Any]
