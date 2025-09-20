from typing import (
    Any,
    Callable,
    Optional,
)

from invenio_records_resources.records.api import Record
from marshmallow.fields import Field

def ensure_no_field_cls(func: Callable) -> Callable: ...

class BaseCF:
    def __init__(self, name: str, field_args: Optional[Any] = ...): ...
    def dump(self, record: Record, cf_key: str = ...): ...
    def load(self, record: Record, cf_key: str = ...): ...

class BaseListCF:
    def __init__(self, name: str, field_cls: Any, multiple: bool = ..., **kwargs): ...
    @property
    def field(self) -> Field: ...
