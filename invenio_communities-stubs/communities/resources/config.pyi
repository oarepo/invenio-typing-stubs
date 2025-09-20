from typing import Any, Dict

from invenio_communities.communities.resources.args import (
    CommunitiesSearchRequestArgsSchema as CommunitiesSearchRequestArgsSchema,
)
from invenio_communities.communities.resources.serializer import (
    UICommunityJSONSerializer as UICommunityJSONSerializer,
)
from invenio_communities.errors import CommunityDeletedError as CommunityDeletedError
from invenio_communities.errors import (
    CommunityFeaturedEntryDoesNotExistError as CommunityFeaturedEntryDoesNotExistError,
)
from invenio_communities.errors import LogoNotFoundError as LogoNotFoundError
from invenio_communities.errors import LogoSizeLimitError as LogoSizeLimitError
from invenio_communities.errors import (
    OpenRequestsForCommunityDeletionError as OpenRequestsForCommunityDeletionError,
)
from invenio_communities.errors import (
    SetDefaultCommunityError as SetDefaultCommunityError,
)
from invenio_records_resources.resources import RecordResourceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_requests.resources.requests.config import RequestSearchRequestArgsSchema

community_error_handlers: dict[type, Any]

class CommunityResourceConfig(RecordResourceConfig, ConfiguratorMixin):
    blueprint_name: Any
    url_prefix: Any
    routes: Dict[str, str]
    request_search_args = CommunitiesSearchRequestArgsSchema
    request_view_args: dict[str, Any]
    error_handlers: Any
    request_community_requests_search_args = RequestSearchRequestArgsSchema
    response_handlers: dict[str, Any]
