from typing import Any, Dict, List, Optional

from invenio_records_resources.records.api import (
    Record,
)
from invenio_records_resources.services.base.links import (
    EndpointLink,
    Link,
)

def pagination_endpoint_links(
    endpoint: str, params: Optional[List[str]] = ...
) -> Dict[str, EndpointLink]: ...
def pagination_links(tpl: str) -> Dict[str, Link]: ...

class RecordLink(Link):
    @staticmethod
    def vars(record: Record, vars: Dict[str, Any]): ...

class RecordEndpointLink(EndpointLink):
    def __init__(self, *args: Any, **kwargs: Any): ...
    @staticmethod
    def vars(obj: Any, vars: Dict[str, Any]): ...
