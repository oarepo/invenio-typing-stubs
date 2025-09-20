from typing import Any, Dict, List, Optional

from flask_principal import Identity
from invenio_records_resources.services.records.queryparser.query import QueryParser
from opensearch_dsl.query import MultiMatch  # type: ignore[import-untyped]

class SuggestQueryParser(QueryParser):
    def __init__(
        self,
        identity: Optional[Identity] = ...,
        extra_params: Optional[Dict[str, List[str]]] = ...,
        **kwargs,
    ): ...
    def parse(self, query_str: str) -> MultiMatch: ...

class CompositeSuggestQueryParser(QueryParser):
    def __init__(
        self,
        identity: Optional[Identity] = None,
        extra_params: Optional[Dict[str, List[str]]] = None,
        clauses: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ): ...
    def extract_subtypes(self, query_str: str) -> tuple[Any, str]: ...
