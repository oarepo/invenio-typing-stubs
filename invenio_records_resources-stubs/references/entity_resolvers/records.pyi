from typing import Any

from invenio_records_resources.references.entity_resolvers.base import (
    EntityProxy as EntityProxy,
)
from invenio_records_resources.references.entity_resolvers.base import (
    EntityResolver as EntityResolver,
)

class RecordProxy(EntityProxy):
    record_cls: type[Any]
    def __init__(
        self, resolver: EntityResolver, ref_dict: dict[str, Any], record_cls: type[Any]
    ) -> None: ...
    def get_needs(self, ctx: Any = None) -> list[Any]: ...
    def pick_resolved_fields(
        self, identity: Any, resolved_dict: dict[str, Any]
    ) -> dict[str, Any]: ...

class RecordPKProxy(RecordProxy): ...

class RecordResolver(EntityResolver):
    record_cls: type[Any]
    type_key: str
    proxy_cls: type[RecordProxy]
    def __init__(
        self,
        record_cls: type[Any],
        service_id: str,
        type_key: str = "record",
        proxy_cls: type[RecordProxy] = ...,
    ) -> None: ...
    def matches_entity(self, entity: Any) -> bool: ...
    def matches_reference_dict(self, ref_dict: dict[str, Any]) -> bool: ...
