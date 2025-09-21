from typing import Any, Callable, Dict, List, Tuple, Type

import marshmallow as ma
from invenio_indexer.api import RecordIndexer  # type: ignore[import-untyped]
from invenio_records.dumpers import Dumper
from invenio_records_permissions.policies.records import RecordPermissionPolicy
from invenio_records_resources.records import Record
from invenio_records_resources.services.base import ServiceConfig
from invenio_records_resources.services.base.links import Link
from invenio_records_resources.services.records.components.base import (
    ServiceComponent,
)
from invenio_records_resources.services.records.params import (
    ParamInterpreter,
)
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_records_resources.services.records.results import (
    RecordBulkItem,
    RecordBulkList,
    RecordItem,
    RecordList,
)
from invenio_search import RecordsSearchV2  # type: ignore[import-untyped]

class SearchOptions:
    """Search options."""

    search_cls: Type[RecordsSearchV2]
    query_parser_cls: Type[QueryParser]
    suggest_parser_cls: Any | None
    sort_default = "bestmatch"
    sort_default_no_query = "newest"
    sort_options: Dict[str, Dict[str, Any]]
    facets: Dict[str, Any]
    pagination_options: Dict[str, Any]
    params_interpreters_cls: (
        List[Type[ParamInterpreter]] | Tuple[Type[ParamInterpreter], ...]
    )

class RecordServiceConfig(ServiceConfig):
    """Service factory configuration."""

    # Common configuration
    service_id: str | None
    permission_policy_cls: type[RecordPermissionPolicy]  # type: ignore[assignment]
    result_item_cls: type[RecordItem]  # type: ignore[assignment]
    result_list_cls: type[RecordList]  # type: ignore[assignment]
    result_bulk_item_cls: type[RecordBulkItem]  # type: ignore[assignment]
    result_bulk_list_cls: type[RecordBulkList]  # type: ignore[assignment]

    # Record specific configuration
    record_cls: type[Record]
    indexer_cls: type[RecordIndexer]
    indexer_queue_name: str
    index_dumper: Dumper | None
    # inverse relation mapping, stores which fields relate to which record type
    relations: Dict[str, List[str]]

    # Search configuration
    search = SearchOptions

    # Service schema
    schema: type[ma.Schema]

    # Definition of those is left up to implementations
    links_item: Dict[str, Callable[..., Any] | Link]
    links_search: Dict[str, Callable[..., Any] | Link]

    # Service components
    components: List[Type[ServiceComponent]] | Tuple[Type[ServiceComponent], ...]  # type: ignore[assignment]
