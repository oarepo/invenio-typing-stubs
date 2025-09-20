from typing import Any, Callable, Dict

from invenio_records_permissions.policies.records import (
    RecordPermissionPolicy as _RecordPermissionPolicy,
)
from invenio_records_resources.services import RecordServiceConfig, SearchOptions
from invenio_records_resources.services.base.config import (
    ConfiguratorMixin,
    SearchOptionsMixin,
)
from invenio_records_resources.services.records.components.base import (
    ServiceComponent as _ServiceComponent,
)
from invenio_requests.customizations import RequestActions as RequestActions
from invenio_requests.records.api import Request as Request
from invenio_requests.services.permissions import PermissionPolicy as PermissionPolicy
from invenio_requests.services.requests import facets as facets
from invenio_requests.services.requests.components import (
    EntityReferencesComponent as EntityReferencesComponent,
)
from invenio_requests.services.requests.components import (
    RequestDataComponent as RequestDataComponent,
)
from invenio_requests.services.requests.components import (
    RequestNumberComponent as RequestNumberComponent,
)
from invenio_requests.services.requests.components import (
    RequestPayloadComponent as RequestPayloadComponent,
)
from invenio_requests.services.requests.components import (
    RequestReviewersComponent as RequestReviewersComponent,
)
from invenio_requests.services.requests.links import RequestLink as RequestLink
from invenio_requests.services.requests.params import IsOpenParam as IsOpenParam
from invenio_requests.services.requests.params import (
    ReferenceFilterParam as ReferenceFilterParam,
)
from invenio_requests.services.requests.params import (
    SharedOrMyRequestsParam as SharedOrMyRequestsParam,
)
from invenio_requests.services.requests.results import RequestItem as RequestItem
from invenio_requests.services.requests.results import RequestList as RequestList
from marshmallow import Schema as _Schema

def _is_action_available(request: Request, context: Dict[str, Any]) -> bool: ...

class RequestSearchOptions(SearchOptions, SearchOptionsMixin):
    facets: Dict[str, Any]

class UserRequestSearchOptions(RequestSearchOptions): ...

class RequestsServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    permission_policy_cls: type[_RecordPermissionPolicy]
    result_item_cls: type[RequestItem]  # type: ignore[assignment]
    result_list_cls: type[RequestList]  # type: ignore[assignment]
    search: type[RequestSearchOptions]
    search_user_requests: type[UserRequestSearchOptions]
    record_cls = Request
    schema: type[_Schema]
    indexer_queue_name: str
    index_dumper: Any
    links_item: Dict[str, Callable[..., Any]]
    links_search: Dict[str, Callable[..., Any]]
    links_user_requests_search: Dict[str, Callable[..., Any]]
    action_link: Any
    payload_schema_cls: type
    components: list[_ServiceComponent] | tuple[_ServiceComponent, ...]  # type: ignore[assignment]
