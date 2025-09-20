from typing import Any, Sequence

from invenio_access import Permission
from invenio_records_permissions.generators import Generator
from invenio_search.engine import dsl

class BasePermissionPolicy(Permission):
    can_search: Sequence[Generator]
    can_create: Sequence[Generator]
    can_read: Sequence[Generator]
    can_update: Sequence[Generator]
    can_delete: Sequence[Generator]
    action: str
    over: dict[str, Any]
    def __init__(self, action: str, **over: Any) -> None: ...
    @property
    def query_filters(self) -> Sequence[dsl.query.Query]: ...
