from typing import Any, Sequence

from invenio_communities.generators import CommunityOwners as CommunityOwners
from invenio_communities.subcommunities.services.request import (
    SubCommunityRequest as SubCommunityRequest,
)
from invenio_records_permissions.generators import Generator
from invenio_records_permissions.policies import BasePermissionPolicy
from invenio_records_resources.services.base.config import (
    ConfiguratorMixin,
    FromConfig,
    ServiceConfig,
)
from invenio_records_resources.services.base.results import ServiceItemResult

from .schema import SubcommunityRequestSchema as SubcommunityRequestSchema

class SubCommunityPermissionPolicy(BasePermissionPolicy):
    can_request_join: Sequence[Generator]
    can_read: Sequence[Generator]
    can_create: Sequence[Generator]
    can_search: Sequence[Generator]
    can_update: Sequence[Generator]
    can_delete: Sequence[Generator]

class SubCommunityServiceConfig(ServiceConfig, ConfiguratorMixin):
    service_id = "subcommunities"
    permission_policy_cls = SubCommunityPermissionPolicy
    result_item_cls: type[ServiceItemResult]
    schema: FromConfig
    request_cls: FromConfig
    links_item: dict[str, Any]
