from collections.abc import Generator

from _typeshed import Incomplete
from invenio_vocabularies.datastreams.factories import (
    DataStreamFactory as DataStreamFactory,
)
from invenio_vocabularies.proxies import current_service as current_service

class VocabularyFixture:
    def __init__(self, filepath, delay: bool = True) -> None: ...
    def load(self, *args, **kwargs) -> Generator[Incomplete]: ...
