import uuid
from typing import Callable

from _typeshed import Incomplete
from invenio_pidstore.models import PersistentIdentifier  # type: ignore[import-untyped]
from invenio_records_resources.records.api import (
    PersistentIdentifierWrapper,
    Record,
)

class UUIDResolver(object):
    object_getter: Callable[[uuid.UUID], Incomplete] | None

    def __init__(
        self,
        getter: Callable[[uuid.UUID], Incomplete] | None = None,
        **kwargs: Incomplete,
    ) -> None: ...
    def resolve(
        self, pid_value: str | uuid.UUID
    ) -> tuple[PersistentIdentifier, Incomplete]: ...

class ModelResolver(object):
    _record_cls: type[Record]
    model_field_name: str

    def __init__(
        self, record_cls: type[Record], model_field_name: str, **kwargs: Incomplete
    ) -> None: ...
    def resolve(
        self, pid_value: str
    ) -> tuple[PersistentIdentifier | PersistentIdentifierWrapper, Record]: ...
