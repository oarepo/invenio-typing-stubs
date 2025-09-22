import uuid
from typing import Any, Callable, Optional, Tuple, Union

from invenio_pidstore.models import PersistentIdentifier  # type: ignore[import-untyped]
from invenio_records.api import Record

class UUIDResolver(object):
    object_getter: Optional[Callable[[uuid.UUID], Any]]

    def __init__(
        self, getter: Optional[Callable[[uuid.UUID], Any]] = None, **kwargs: Any
    ) -> None: ...
    def resolve(
        self, pid_value: Union[str, uuid.UUID]
    ) -> Tuple[PersistentIdentifier, Any]: ...

class ModelResolver(object):
    _record_cls: type[Record]
    model_field_name: str

    def __init__(
        self, record_cls: type[Record], model_field_name: str, **kwargs: Any
    ) -> None: ...
    def resolve(self, pid_value: str) -> Tuple[Any, Record]: ...
