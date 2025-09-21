from typing import Any

from invenio_records_resources.references.entity_resolvers.base import (
    EntityProxy as EntityProxy,
)
from invenio_records_resources.references.entity_resolvers.base import (
    EntityResolver as EntityResolver,
)

class ServiceResultProxy(EntityProxy):
    service: Any  # Service
    def __init__(
        self, resolver: EntityResolver, ref_dict: dict[str, Any], service: Any
    ) -> None: ...
    def _resolve(self) -> Any: ...
    def get_needs(self, ctx: Any = None) -> list[Any]: ...
    def pick_resolved_fields(
        self, identity: Any, resolved_dict: dict[str, Any]
    ) -> dict[str, Any]: ...

class ServiceResultResolver(EntityResolver):
    type_key: str
    proxy_cls: type[ServiceResultProxy]
    def __init__(
        self,
        service_id: str,
        type_key: str,
        proxy_cls: type[ServiceResultProxy] = ...,
        item_cls: type[Any] | None = None,
        record_cls: type[Any] | None = None,
    ) -> None: ...
    @property
    def item_cls(self) -> type[Any] | None: ...
    @property
    def record_cls(self) -> type[Any] | None: ...
    def matches_entity(self, entity: Any) -> bool: ...
    def matches_reference_dict(self, ref_dict: dict[str, Any]) -> bool: ...
    def _reference_entity(self, entity: Any) -> dict[str, Any]: ...
    def _get_entity_proxy(self, ref_dict: dict[str, Any]) -> ServiceResultProxy: ...
