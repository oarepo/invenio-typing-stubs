from typing import Any, Callable

from _typeshed import Incomplete
from invenio_records.systemfields import SystemField
from invenio_records_resources.references.entity_resolvers import EntityProxy

class ReferencedEntityField(SystemField):
    _ref_check: Callable[[Incomplete, dict[str, str] | None], bool] | None
    _registry: Incomplete

    def __init__(
        self,
        key: str | None = ...,
        reference_check_func: (
            Callable[[Incomplete, dict[str, str] | None], bool] | None
        ) = ...,
        resolver_registry: Incomplete = ...,
    ) -> None: ...
    def _check_reference(
        self, instance: Incomplete, ref_dict: dict[str, str] | None
    ) -> bool: ...
    def set_obj(
        self,
        instance: Incomplete,
        obj: dict[str, str] | EntityProxy | Incomplete | None,
    ) -> None: ...
    def obj(self, instance: Incomplete) -> Incomplete: ...
    def __get__(self, record: Incomplete, owner: Any = ...) -> Any: ...
    def __set__(self, record: Incomplete, value: Incomplete) -> None: ...

class MultiReferenceEntityField(ReferencedEntityField):
    def set_obj(self, instance: Incomplete, obj: Incomplete) -> None: ...
    def obj(self, instance: Incomplete) -> list[EntityProxy]: ...

def check_allowed_references(
    get_allows_none: Callable[[Incomplete], bool],
    get_allowed_types: Callable[[Incomplete], list[str]],
    request: Incomplete,
    ref_dict: dict[str, str] | None,
) -> bool: ...
