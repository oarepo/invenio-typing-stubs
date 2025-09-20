from typing import Optional, Sequence, TypedDict

from flask_principal import Identity
from invenio_communities.communities.records.api import Community
from invenio_communities.generators import AllowedMemberTypes as AllowedMemberTypes
from invenio_communities.generators import (
    AuthenticatedButNotCommunityMembers as AuthenticatedButNotCommunityMembers,
)
from invenio_communities.generators import CommunityCurators as CommunityCurators
from invenio_communities.generators import CommunityManagers as CommunityManagers
from invenio_communities.generators import (
    CommunityManagersForRole as CommunityManagersForRole,
)
from invenio_communities.generators import CommunityMembers as CommunityMembers
from invenio_communities.generators import CommunityOwners as CommunityOwners
from invenio_communities.generators import CommunitySelfMember as CommunitySelfMember
from invenio_communities.generators import IfCommunityDeleted as IfCommunityDeleted
from invenio_communities.generators import IfMemberPolicyClosed as IfMemberPolicyClosed
from invenio_communities.generators import (
    IfRecordSubmissionPolicyClosed as IfRecordSubmissionPolicyClosed,
)
from invenio_communities.generators import IfRestricted as IfRestricted
from invenio_communities.generators import ReviewPolicy as ReviewPolicy
from invenio_records_permissions.generators import Generator
from invenio_records_permissions.policies import BasePermissionPolicy

class CommunityPermissionPolicy(BasePermissionPolicy):
    """Permissions for Community CRUD operations."""

    can_create: Sequence[Generator]
    can_read: Sequence[Generator]
    can_read_deleted: Sequence[Generator]
    can_update: Sequence[Generator]
    can_delete: Sequence[Generator]
    can_purge: Sequence[Generator]
    can_manage_access: Sequence[Generator]
    can_create_restricted: Sequence[Generator]
    can_search: Sequence[Generator]
    can_search_user_communities: Sequence[Generator]
    can_search_invites: Sequence[Generator]
    can_search_requests: Sequence[Generator]
    can_rename: Sequence[Generator]
    can_submit_record: Sequence[Generator]
    can_include_directly: Sequence[Generator]
    can_members_add: Sequence[Generator]
    can_members_invite: Sequence[Generator]
    can_members_manage: Sequence[Generator]
    can_members_search: Sequence[Generator]
    can_members_search_public: Sequence[Generator]
    can_members_bulk_update: Sequence[Generator]
    can_members_bulk_delete = can_members_bulk_update
    can_members_update: Sequence[Generator]
    can_members_delete = can_members_update
    can_invite_owners: Sequence[Generator]
    can_featured_search: Sequence[Generator]
    can_featured_list: Sequence[Generator]
    can_featured_create: Sequence[Generator]
    can_featured_update: Sequence[Generator]
    can_featured_delete: Sequence[Generator]
    can_moderate: Sequence[Generator]
    can_set_theme: Sequence[Generator]
    can_delete_theme = can_set_theme
    can_manage_children: Sequence[Generator]
    can_manage_parent: Sequence[Generator]
    can_request_membership: Sequence[Generator]

class PermissionContext(TypedDict, total=False):
    action: str
    identity: Optional[Identity]
    permission_policy_cls: type[BasePermissionPolicy]

def can_perform_action(community: Community, context: PermissionContext) -> bool: ...
