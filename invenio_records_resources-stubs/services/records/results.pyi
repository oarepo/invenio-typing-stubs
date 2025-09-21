from abc import ABC, abstractmethod
from typing import (
    Any,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
)

from flask_principal import (
    Identity,
)
from invenio_records_resources.pagination import Pagination
from invenio_records_resources.records.api import (
    Record,
)
from invenio_records_resources.services.base import Service
from invenio_records_resources.services.base.links import Link, LinksTemplate
from invenio_records_resources.services.base.results import (
    ServiceBulkItemResult,
    ServiceBulkListResult,
    ServiceItemResult,
    ServiceListResult,
)
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_records_resources.services.records.service import RecordService

class ExpandableField(ABC):
    def __init__(self, field_name: str): ...
    @property
    def field_name(self) -> str: ...
    @abstractmethod
    def get_value_service(self, value: Any) -> Any: ...
    @abstractmethod
    def ghost_record(self, value: Any) -> Any: ...
    @abstractmethod
    def system_record(self) -> Any: ...
    def has(self, service: Service, value: Any) -> bool: ...
    def add_service_value(self, service: Service, value: Any) -> None: ...
    def add_dereferenced_record(
        self, service: Service, value: Any, resolved_rec: Any
    ) -> None: ...
    def get_dereferenced_record(self, service: Service, value: Any) -> Any: ...
    @abstractmethod
    def pick(self, identity: Identity, resolved_rec: Any) -> Any: ...

class FieldsResolver:
    def __init__(self, expandable_fields: Optional[List[ExpandableField]]): ...
    def resolve(
        self,
        identity: Identity,
        hits: Iterable[Dict[str, Any]],
    ) -> None: ...
    def expand(
        self,
        identity: Identity,
        hit: Dict[str, Any],
    ) -> Dict[str, Any]: ...

class MultiFieldsResolver(FieldsResolver): ...

class RecordBulkItem(ServiceBulkItemResult):
    def __init__(
        self,
        op_type: str,
        record: Record,
        errors: Optional[List[Any]],
        exc: Optional[BaseException],
    ): ...
    @property
    def errors(self) -> Optional[List[Any]]: ...
    @property
    def op_type(self) -> str: ...
    @property
    def record(
        self,
    ) -> Record: ...
    @property
    def exc(self) -> Optional[BaseException]: ...

class RecordBulkList(ServiceBulkListResult):
    def __init__(self, service: Service, identity: Identity, results: List[Any]): ...
    @property
    def results(self) -> Iterator[RecordBulkItem]: ...

class RecordItem(ServiceItemResult):
    _service: RecordService  # keep typing
    _identity: Identity  # keep typing
    _record: Record  # keep typing
    _errors: Optional[List[Any]]  # keep typing
    _links_tpl: Optional[LinksTemplate]  # keep typing
    _schema: ServiceSchemaWrapper  # keep typing
    _expandable_fields: Optional[List[ExpandableField]]  # keep typing
    _expand: bool  # keep typing
    _nested_links_item: Optional[List[Link]]  # keep typing
    _data: Optional[Dict[str, Any]]  # keep typing

    def __getitem__(self, key: str) -> Any: ...
    def __init__(
        self,
        service: Service,
        identity: Identity,
        record: Record,
        errors: Optional[List[Any]] = ...,
        links_tpl: Optional[LinksTemplate] = ...,
        schema: Optional[ServiceSchemaWrapper] = ...,
        expandable_fields: Optional[List[ExpandableField]] = ...,
        expand: bool = ...,
        nested_links_item: Optional[List[Link]] = ...,
    ): ...
    @property
    def _obj(self) -> Record: ...
    @property
    def data(self) -> Dict[str, Any]: ...
    def has_permissions_to(self, actions: List[str]) -> Dict[str, bool]: ...
    @property
    def id(self) -> str: ...
    @property
    def links(self) -> Dict[str, Any]: ...
    @property
    def errors(self) -> Optional[List[Any]]: ...
    def to_dict(self) -> Dict[str, Any]: ...

class RecordList(ServiceListResult):
    _expand: bool  # keep typing
    _identity: Identity  # keep typing
    _fields_resolver: Optional[FieldsResolver]  # keep typing
    _schema: ServiceSchemaWrapper  # keep typing
    _expandable_fields: Optional[List[ExpandableField]]  # keep typing
    _links_tpl: Optional[LinksTemplate]  # keep typing
    _links_item_tpl: Optional[LinksTemplate]  # keep typing
    _nested_links_item: Optional[List[Link]]  # keep typing
    _service: RecordService  # keep typing
    _results: Any  # keep typing

    def __init__(
        self,
        service: RecordService,
        identity: Identity,
        results: Any,
        params: Optional[Dict[str, Any]] = ...,
        links_tpl: Optional[LinksTemplate] = ...,
        links_item_tpl: Optional[LinksTemplate] = ...,
        nested_links_item: Optional[List[Link]] = ...,
        schema: Optional[ServiceSchemaWrapper] = ...,
        expandable_fields: Optional[List[ExpandableField]] = ...,
        expand: bool = ...,
    ): ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    @property
    def aggregations(self) -> Optional[Dict[str, Any]]: ...
    @property
    def hits(self) -> Iterator[Dict[str, Any]]: ...
    @property
    def pagination(self) -> Pagination: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @property
    def total(self) -> Optional[int]: ...
