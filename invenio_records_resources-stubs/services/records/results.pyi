from typing import (
    Any,
    Dict,
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
from invenio_records_resources.services.base.links import LinksTemplate
from invenio_records_resources.services.base.results import (
    ServiceItemResult,
    ServiceListResult,
)
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_records_resources.services.records.service import RecordService
from opensearch_dsl.response import Response  # type: ignore[import-untyped]

class FieldsResolver:
    def __init__(self, expandable_fields: None): ...
    def expand(
        self,
        identity: Identity,
        hit: Dict[
            str,
            Any,
        ],
    ) -> Dict[str, Any]: ...
    def resolve(
        self,
        identity: Identity,
        hits: List[Dict[str, Any]],
    ): ...

class RecordBulkItem:
    def __init__(
        self,
        op_type: str,
        record: Record,
        errors: List[Any],
        exc: None,
    ): ...
    @property
    def errors(self) -> List[Any]: ...
    @property
    def op_type(self) -> str: ...
    @property
    def record(
        self,
    ) -> Record: ...

class RecordBulkList:
    def __init__(self, service: Service, identity: Identity, results: List[Any]): ...

class RecordItem(ServiceItemResult):
    def __getitem__(self, key: str) -> Any: ...
    def __init__(
        self,
        service: Service,
        identity: Identity,
        record: Record,
        errors: Optional[List[Any]] = ...,
        links_tpl: Optional[LinksTemplate] = ...,
        schema: Optional[ServiceSchemaWrapper] = ...,
        expandable_fields: None = ...,
        expand: bool = ...,
        nested_links_item: None = ...,
    ): ...
    @property
    def _obj(self) -> Record: ...
    @property
    def data(self) -> Dict[str, Any]: ...
    def has_permissions_to(self, actions: List[str]) -> Dict[str, bool]: ...
    @property
    def id(self) -> str: ...
    @property
    def links(self) -> Dict[str, str]: ...
    def to_dict(self) -> Dict[str, Any]: ...

class RecordList(ServiceListResult):
    def __init__(
        self,
        service: RecordService,
        identity: Identity,
        results: Response,
        params: Optional[Dict[str, Any]] = ...,
        links_tpl: None = ...,
        links_item_tpl: Optional[LinksTemplate] = ...,
        nested_links_item: None = ...,
        schema: None = ...,
        expandable_fields: None = ...,
        expand: bool = ...,
    ): ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    @property
    def aggregations(
        self,
    ) -> Dict[str, Any]: ...
    @property
    def hits(self): ...
    @property
    def pagination(self) -> Pagination: ...
    def to_dict(self) -> Dict[str, Any]: ...
    @property
    def total(self) -> int: ...
