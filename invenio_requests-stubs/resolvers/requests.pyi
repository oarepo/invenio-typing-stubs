from invenio_records_resources.references.entity_resolvers import RecordResolver
from invenio_requests.records.api import Request as Request
from invenio_requests.records.api import RequestEvent as RequestEvent
from invenio_requests.services import (
    RequestEventsServiceConfig as RequestEventsServiceConfig,
)
from invenio_requests.services import RequestsServiceConfig as RequestsServiceConfig

class RequestResolver(RecordResolver):
    type_id: str
    def __init__(self) -> None: ...

class RequestEventResolver(RecordResolver):
    type_id: str
    def __init__(self) -> None: ...
