from typing import Any

from invenio_records_resources.services import RecordServiceConfig, SearchOptions
from invenio_records_resources.services.base.config import ConfiguratorMixin

from ...communities.records.api import Community as Community
from ...permissions import CommunityPermissionPolicy as CommunityPermissionPolicy
from ..records import Member as Member
from ..records.api import ArchivedInvitation as ArchivedInvitation
from . import facets as facets
from .components import (
    CommunityMemberCachingComponent as CommunityMemberCachingComponent,
)
from .schemas import MemberEntitySchema as MemberEntitySchema

class PublicSearchOptions(SearchOptions):
    sort_default: str
    sort_default_no_query: str
    sort_options: dict[str, Any]
    query_parser_cls: Any

class InvitationsSearchOptions(SearchOptions):
    sort_default: str
    sort_default_no_query: str
    sort_options: dict[str, Any]
    facets: dict[str, Any]

class MemberSearchOptions(PublicSearchOptions):
    sort_default: str
    sort_default_no_query: str
    sort_options: dict[str, Any]
    facets: dict[str, Any]
    query_parser_cls: Any

class MemberServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    service_id: str
    community_cls = Community
    record_cls = Member
    schema = MemberEntitySchema
    indexer_queue_name: str
    relations: Any
    archive_cls = ArchivedInvitation
    archive_indexer_cls: Any
    archive_indexer_queue_name: str
    permission_policy_cls: Any
    search = MemberSearchOptions
    search_public = PublicSearchOptions
    search_invitations = InvitationsSearchOptions
    links_item: dict[str, Any]
    links_search: Any
    components: Any
