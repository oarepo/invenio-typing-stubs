from typing import Any, Iterable

from invenio_records_resources.services.base.results import (
    ServiceItemResult,
    ServiceListResult,
)

class SecretLinkItem(ServiceItemResult):
    _errors: Any
    _identity: Any
    _links_config: Any
    _link: Any
    _service: Any
    _data: Any | None
    def __init__(
        self,
        service,
        identity,
        link,
        errors: Any | None = None,
        links_config: Any | None = None,
    ) -> None: ...
    @property
    def id(self) -> str: ...
    @property
    def data(self) -> dict[str, Any]: ...
    def to_dict(self) -> dict[str, Any]: ...

class SecretLinkList(ServiceListResult):
    _service: Any
    _identity: Any
    _results: Iterable[Any]
    _links_config: Any
    def __init__(
        self, service, identity, results: Iterable[Any], links_config: Any | None = None
    ) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def results(self) -> Iterable[dict[str, Any]]: ...
    def to_dict(self) -> dict[str, Any]: ...

class GrantItem(ServiceItemResult):
    _errors: Any
    _identity: Any
    _grant: Any
    _service: Any
    _expand: bool
    _fields_resolver: Any
    _data: Any | None
    def __init__(
        self,
        service,
        identity,
        grant,
        errors: Any | None = None,
        expandable_fields: Any | None = None,
        expand: bool = False,
    ) -> None: ...
    @property
    def data(self) -> dict[str, Any]: ...
    def to_dict(self) -> dict[str, Any]: ...

class GrantList(ServiceListResult):
    _service: Any
    _identity: Any
    _results: Iterable[Any]
    _fields_resolver: Any
    _expand: bool
    def __init__(
        self,
        service,
        identity,
        results: Iterable[Any],
        expandable_fields: Any | None = None,
        expand: bool = False,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    @property
    def results(self) -> Iterable[dict[str, Any]]: ...
    def to_dict(self) -> dict[str, Any]: ...
