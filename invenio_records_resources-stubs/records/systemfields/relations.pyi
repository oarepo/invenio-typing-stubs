from typing import Any, Optional

from invenio_records.systemfields.relations import (
    ListRelation,
    NestedListRelation,
    RelationBase,
)
from invenio_records_resources.records.api import Record

class PIDRelation[R: Record = Record](RelationBase):
    def __init__(self, *args: Any, pid_field: Any = ..., **kwargs: Any) -> None: ...
    def resolve(self, id_: str) -> Optional[R]: ...
    def parse_value(self, value: Any) -> str: ...

class PIDListRelation(ListRelation, PIDRelation):
    """PID list relation type."""

class PIDNestedListRelation(NestedListRelation, PIDRelation):
    """PID nested list relation type."""
