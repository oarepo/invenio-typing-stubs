from typing import Any, Dict, List, Type

from invenio_records_resources.services import SearchOptions
from invenio_records_resources.services.records.components import ServiceComponent
from invenio_records_resources.services.records.queryparser import (
    CompositeSuggestQueryParser,
)
from invenio_vocabularies.services.components import (
    ModelPIDComponent as ModelPIDComponent,
)
from werkzeug.local import LocalProxy

funder_schemes: LocalProxy[Dict[str, Dict[str, Any]]]
funder_fundref_doi_prefix: LocalProxy[str]
localized_title: LocalProxy[str]

class FundersSearchOptions(SearchOptions):
    suggest_parser_cls: Type[CompositeSuggestQueryParser]
    sort_default: str
    sort_default_no_query: str
    sort_options: Dict[str, Dict[str, Any]]

service_components: List[Type[ServiceComponent]]
