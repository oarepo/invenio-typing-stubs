from typing import Any, ClassVar, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import ServiceComponent
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_vocabularies.services.components import (
    ModelPIDComponent as ModelPIDComponent,
)

funder_schemes: Dict[
    str, Dict[str, Any]
]  # intentionally not using a LocalProxy[Dict[str, Dict[str, Any]]] here as mypy does not understand it
funder_fundref_doi_prefix: (
    str  # intentionally not using a LocalProxy[str] here as mypy does not understand it
)
localized_title: (
    str  # intentionally not using a LocalProxy[str] here as mypy does not understand it
)

class FundersSearchOptions(SearchOptions):
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    sort_default: ClassVar[str]
    sort_default_no_query: ClassVar[str]
    sort_options: ClassVar[Dict[str, Dict[str, Any]]]

service_components: List[Type[ServiceComponent]]
