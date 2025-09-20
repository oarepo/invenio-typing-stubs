from typing import Any, Callable

import marshmallow as ma
from invenio_indexer.api import RecordIndexer
from invenio_records.dumpers import Dumper
from invenio_records_permissions.policies.records import RecordPermissionPolicy
from invenio_records_resources.records import Record
from invenio_records_resources.services.base import ServiceConfig
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
from invenio_search import RecordsSearchV2

class SearchOptions:
    """Search options."""

    search_cls: RecordsSearchV2
    query_parser_cls: QueryParser
    suggest_parser_cls: Any = None
    sort_default = "bestmatch"
    sort_default_no_query = "newest"
    sort_options: dict[str, dict[str, Any]]
    facets: dict[str, Any]
    pagination_options: dict[str, Any]
    params_interpreters_cls: list[ParamInterpreter] | tuple[ParamInterpreter, ...]

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
    relations: dict[str, type[Record]]

    # Search configuration
    search = SearchOptions

    # Service schema
    schema: type[ma.Schema]

    # Definition of those is left up to implementations
    links_item: dict[str, Callable[..., Any]]
    links_search: dict[str, Callable[..., Any]]

    # Service components
    components: list[ServiceComponent] | tuple[ServiceComponent, ...]  # type: ignore[assignment]
