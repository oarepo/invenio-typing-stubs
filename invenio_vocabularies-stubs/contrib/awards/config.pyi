from typing import Any, Dict, List

from invenio_records_resources.services import SearchOptions
from invenio_vocabularies.contrib.funders.facets import FundersLabels as FundersLabels
from invenio_vocabularies.services.components import (
    ModelPIDComponent as ModelPIDComponent,
)
from werkzeug.local import LocalProxy

award_schemes: LocalProxy[Dict[str, Dict[str, Any]]]
awards_openaire_funders_mapping: LocalProxy[Dict[str, str]]
awards_ec_ror_id: LocalProxy[str]

class AwardsSearchOptions(SearchOptions):
    suggest_parser_cls: type
    facets: Dict[str, Any]

service_components: List[type]
