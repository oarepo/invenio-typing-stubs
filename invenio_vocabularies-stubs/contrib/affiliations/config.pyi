from typing import Any, Dict, List

from invenio_records_resources.services import SearchOptions
from invenio_vocabularies.services.components import PIDComponent as PIDComponent
from werkzeug.local import LocalProxy

affiliation_schemes: LocalProxy[Dict[str, Dict[str, Any]]]
affiliation_edmo_country_mappings: LocalProxy[Dict[str, str]]
localized_title: LocalProxy[str]

class AffiliationsSearchOptions(SearchOptions):
    suggest_parser_cls: type
    sort_default: str
    sort_default_no_query: str
    sort_options: Dict[str, Dict[str, Any]]

service_components: List[type]
