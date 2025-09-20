from collections.abc import Generator
from typing import Any, List, Optional

from invenio_records_resources.records.api import Record
from invenio_vocabularies.datastreams.errors import ReaderError as ReaderError
from invenio_vocabularies.datastreams.errors import TransformerError as TransformerError
from invenio_vocabularies.datastreams.errors import WriterError as WriterError
from invenio_vocabularies.datastreams.readers import BaseReader
from invenio_vocabularies.datastreams.transformers import BaseTransformer
from invenio_vocabularies.datastreams.writers import BaseWriter

class StreamEntry:
    entry: Any
    record: Optional[Record]
    filtered: bool
    errors: Optional[List[str]]
    op_type: Optional[str]
    exc: Optional[Exception]
    def __init__(
        self,
        entry: Any,
        record=None,
        errors: Optional[List[str]] = None,
        op_type=None,
        exc=None,
    ) -> None: ...
    def log_errors(self, logger=None) -> None: ...

class DataStream:
    batch_size: int
    write_many: bool
    def __init__(
        self,
        readers: List[BaseReader],
        writers: List[BaseWriter],
        transformers: Optional[List[BaseTransformer]] = None,
        batch_size: int = 100,
        write_many: bool = False,
        *args,
        **kwargs,
    ) -> None: ...
    def filter(self, stream_entry: StreamEntry, *args, **kwargs) -> bool: ...
    def process_batch(
        self, batch: List[StreamEntry]
    ) -> Generator[StreamEntry, None, None]: ...
    def process(self, *args, **kwargs) -> Generator[StreamEntry, None, None]: ...
    def read(self) -> Generator[StreamEntry, None, None]: ...
    def transform(self, stream_entry: StreamEntry, *args, **kwargs) -> StreamEntry: ...
    def write(self, stream_entry: StreamEntry, *args, **kwargs) -> StreamEntry: ...
    def batch_write(
        self, stream_entries, *args, **kwargs
    ) -> Generator[StreamEntry, None, None]: ...
    def total(self, *args, **kwargs) -> int: ...
