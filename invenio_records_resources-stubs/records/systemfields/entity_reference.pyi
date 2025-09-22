from typing import Any, Callable, Dict, List, Optional, Union

from invenio_records.systemfields import SystemField
from invenio_records_resources.references.entity_resolvers import EntityProxy

class ReferencedEntityField(SystemField):
    _ref_check: Optional[Callable[[Any, Optional[Dict[str, str]]], bool]]
    _registry: Any

    def __init__(
        self,
        key: Optional[str] = ...,
        reference_check_func: Optional[
            Callable[[Any, Optional[Dict[str, str]]], bool]
        ] = ...,
        resolver_registry: Any = ...,
    ) -> None: ...
    def _check_reference(
        self, instance: Any, ref_dict: Optional[Dict[str, str]]
    ) -> bool: ...
    def set_obj(
        self, instance: Any, obj: Union[Dict[str, str], EntityProxy, Any, None]
    ) -> None: ...
    def obj(self, instance: Any) -> Optional[EntityProxy]: ...
    def __get__(self, record: Any, owner: Any = ...) -> Any: ...
    def __set__(self, record: Any, value: Any) -> None: ...

class MultiReferenceEntityField(ReferencedEntityField):
    def set_obj(self, instance: Any, obj: Any) -> None: ...
    def obj(self, instance: Any) -> Any: ...

def check_allowed_references(
    get_allows_none: Callable[[Any], bool],
    get_allowed_types: Callable[[Any], List[str]],
    request: Any,
    ref_dict: Optional[Dict[str, str]],
) -> bool: ...
