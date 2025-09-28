from typing import Any, ClassVar, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import (
    ServiceComponent as ServiceComponent,
)
from invenio_records_resources.services.records.facets import TermsFacet
from invenio_records_resources.services.records.params import QueryParser
from invenio_vocabularies.contrib.funders.facets import FundersLabels as FundersLabels

award_schemes: Dict[
    str, Dict[str, Any]
]  # intentionally not using a LocalProxy[Dict[str, Dict[str, Any]]] here as mypy does not understand it
awards_openaire_funders_mapping: Dict[
    str, str
]  # intentionally not using a LocalProxy[Dict[str, str]] here as mypy does not understand it
awards_ec_ror_id: (
    str  # intentionally not using a LocalProxy[str] here as mypy does not understand it
)

class AwardsSearchOptions(SearchOptions):
    suggest_parser_cls: ClassVar[type[QueryParser] | None]
    facets: ClassVar[Dict[str, TermsFacet]]

service_components: List[Type[ServiceComponent]]
