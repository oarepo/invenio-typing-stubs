from typing import Dict

from invenio_records_resources.references.entity_resolvers import (
    RecordPKProxy,
    RecordResolver,
)

from ..generators import CommunityRoleNeed as CommunityRoleNeed
from ..proxies import current_communities as current_communities
from ..proxies import current_roles as current_roles
from .records.api import Community as Community
from .schema import CommunityGhostSchema as CommunityGhostSchema
from .services.config import CommunityServiceConfig as CommunityServiceConfig

def pick_fields(identity, community_dict): ...

class CommunityPKProxy(RecordPKProxy):
    def ghost_record(self, value): ...
    def get_needs(self, ctx=None): ...
    def pick_resolved_fields(self, identity, resolved_dict): ...

class CommunityResolver(RecordResolver):
    type_id: str
    def __init__(self) -> None: ...
    def _reference_entity(self, entity: Community) -> Dict[str, str]: ...
