from typing import Any, Dict

from invenio_records_resources.records.api import (
    Record,
)
from invenio_records_resources.services.base.links import (
    EndpointLink,
    Link,
)

def pagination_endpoint_links(
    endpoint: str, params: None = ...
) -> Dict[str, EndpointLink]: ...
def pagination_links(tpl: str) -> Dict[str, Link]: ...

class RecordLink(Link):
    @staticmethod
    def vars(record: Record, vars: Dict[str, Any]): ...

class RecordEndpointLink:
    def __init__(self, *args, **kwargs): ...
    @staticmethod
    def vars(record: Record, vars: Dict[str, Any]): ...
