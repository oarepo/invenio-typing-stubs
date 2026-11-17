from datetime import datetime
from typing import Any, Dict, Generic, Optional, Type, TypeVar
from uuid import UUID

from flask_principal import Identity
from invenio_communities.communities.records.api import Community
from invenio_communities.members.errors import AlreadyMemberError as AlreadyMemberError
from invenio_communities.members.errors import InvalidMemberError as InvalidMemberError
from invenio_communities.members.records.api import (
    ArchivedInvitation as ArchivedInvitation,
)
from invenio_communities.members.records.api import (
    ArchivedMemberRequest as ArchivedMemberRequest,
)
from invenio_communities.members.records.api import Member
from invenio_communities.members.records.api import MemberMixin as MemberMixin
from invenio_communities.members.services.config import MemberServiceConfig
from invenio_communities.members.services.request import (
    CommunityInvitation as CommunityInvitation,
)
from invenio_communities.members.services.request import (
    MembershipRequestRequestType as MembershipRequestRequestType,
)
from invenio_communities.members.services.schemas import (
    AddBulkSchema as AddBulkSchema,
)
from invenio_communities.members.services.schemas import (
    DeleteBulkSchema as DeleteBulkSchema,
)
from invenio_communities.members.services.schemas import (
    InvitationDumpSchema as InvitationDumpSchema,
)
from invenio_communities.members.services.schemas import (
    InviteBulkSchema as InviteBulkSchema,
)
from invenio_communities.members.services.schemas import (
    MemberDumpSchema as MemberDumpSchema,
)
from invenio_communities.members.services.schemas import (
    MembershipRequestDumpSchema as MembershipRequestDumpSchema,
)
from invenio_communities.members.services.schemas import (
    PublicDumpSchema as PublicDumpSchema,
)
from invenio_communities.members.services.schemas import (
    RequestMembershipSchema as RequestMembershipSchema,
)
from invenio_communities.members.services.schemas import (
    UpdateBulkSchema as UpdateBulkSchema,
)
from invenio_communities.notifications.builders import (
    CommunityInvitationSubmittedNotificationBuilder as CommunityInvitationSubmittedNotificationBuilder,
)
from invenio_communities.notifications.builders import (
    CommunityMembershipRequestSubmittedNotificationBuilder as CommunityMembershipRequestSubmittedNotificationBuilder,
)
from invenio_communities.proxies import current_roles as current_roles
from invenio_communities.roles import Role
from invenio_db.uow import UnitOfWork
from invenio_indexer.api import RecordIndexer
from invenio_records_resources.services import LinksTemplate
from invenio_records_resources.services.records import (
    RecordService,
    ServiceSchemaWrapper,
)
from invenio_records_resources.services.records.results import RecordList
from invenio_requests.services.requests.results import RequestItem

def invite_expires_at() -> datetime: ...

C = TypeVar("C", bound=MemberServiceConfig)

class MemberService(RecordService[C], Generic[C]):
    @property
    def community_cls(self) -> Type[Community]: ...
    @property
    def archive_cls(self) -> Type[ArchivedMemberRequest]: ...
    @property
    def member_dump_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def public_dump_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def invitation_dump_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def add_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def invite_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def update_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def delete_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def request_membership_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def archive_indexer(self) -> RecordIndexer: ...
    def _add_factory(
        self,
        identity: Identity,
        community: Community,
        role: Role,
        visible: bool,
        member: Dict[str, Any],
        message: Optional[str],
        uow: UnitOfWork,
        active: bool = ...,
        request_id: Optional[str] = ...,
        **kwargs: Any,
    ) -> None: ...
    def _invite_factory(
        self,
        identity: Identity,
        community: Community,
        role: Role,
        visible: bool,
        member: Dict[str, Any],
        message: Optional[str],
        uow: UnitOfWork,
        **kwargs: Any,
    ) -> None: ...
    def _members_search(
        self,
        identity: Identity,
        community_id: str,
        permission_action: str,
        schema: ServiceSchemaWrapper,
        search_opts: Type[Any],
        extra_filter: Optional[Any] = ...,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        links_tpl: Optional[LinksTemplate] = ...,
        scan: bool = ...,
        scan_params: Optional[Dict[str, Any]] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def _update(
        self,
        identity: Identity,
        community: Community,
        member: Member,
        role: Optional[Role],
        visible: Optional[bool],
        group_notification_enabled: Optional[bool],
        uow: UnitOfWork,
    ) -> bool: ...
    def add(
        self,
        identity: Identity,
        community_id: str | UUID,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> bool: ...
    def delete(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str | UUID,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> bool: ...
    def invite(
        self,
        identity: Identity,
        community_id: str | UUID,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> bool: ...
    def read_memberships(self, identity: Identity) -> Dict[str, Any]: ...
    def request_membership(
        self,
        identity: Identity,
        community_id: str | UUID,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> RequestItem: ...
    def scan(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str | UUID,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        extra_filter: Optional[Any] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def search(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str | UUID,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        extra_filter: Optional[Any] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def search_invitations(
        self,
        identity: Identity,
        community_id: str | UUID,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def search_public(
        self,
        identity: Identity,
        community_id: str | UUID,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def update(  # type: ignore[override]
        self,
        identity: Identity,
        community_id: str | UUID,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
        refresh: bool = ...,
    ) -> bool: ...
    def search_membership_requests(
        self,
        identity: Identity,
        community_id: str | UUID,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def accept_member_request(
        self,
        identity: Identity,
        request_id: str | UUID,
        uow: Optional[UnitOfWork] = ...,
    ) -> None: ...
    def close_member_request(
        self,
        identity: Identity,
        request_id: str | UUID,
        uow: Optional[UnitOfWork] = ...,
    ) -> None: ...
    def get_request_id_of_pending_member(
        self, identity: Identity, community_id: str | UUID
    ) -> Optional[UUID]: ...
    def rebuild_index(
        self, identity: Identity, uow: Optional[UnitOfWork] = ...
    ) -> bool: ...
