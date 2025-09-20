import uuid
from typing import Any, Callable, Optional

from invenio_pidstore.models import PersistentIdentifier
from invenio_records.api import Record

class UUIDResolver(object):
    def __init__(
        self, getter: Optional[Callable[[uuid.UUID], Any]] = None, **kwargs: Any
    ): ...
    def resolve(self, pid_value: str) -> tuple[PersistentIdentifier, Any]: ...

class ModelResolver(object):
    def __init__(
        self, record_cls: type[Record], model_field_name: str, **kwargs: Any
    ): ...
    def resolve(self, pid_value: str) -> tuple[PersistentIdentifier, Any]: ...
