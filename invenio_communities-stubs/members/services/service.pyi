from datetime import datetime
from typing import Any, Dict, Optional, Type

from flask_principal import Identity
from invenio_communities.communities.records.api import Community
from invenio_communities.members.records.api import Member
from invenio_communities.roles import Role
from invenio_db.uow import UnitOfWork
from invenio_indexer.api import RecordIndexer
from invenio_records_resources.services.records import RecordService
from invenio_records_resources.services.records.results import RecordList
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from invenio_requests.services.requests.results import RequestItem
from opensearch_dsl.query import Terms

from ...notifications.builders import (
    CommunityInvitationSubmittedNotificationBuilder as CommunityInvitationSubmittedNotificationBuilder,
)
from ...proxies import current_roles as current_roles
from ..errors import AlreadyMemberError as AlreadyMemberError
from ..errors import InvalidMemberError as InvalidMemberError
from ..records.api import ArchivedInvitation as ArchivedInvitation
from .request import CommunityInvitation as CommunityInvitation
from .request import MembershipRequestRequestType as MembershipRequestRequestType
from .schemas import AddBulkSchema as AddBulkSchema
from .schemas import DeleteBulkSchema as DeleteBulkSchema
from .schemas import InvitationDumpSchema as InvitationDumpSchema
from .schemas import InviteBulkSchema as InviteBulkSchema
from .schemas import MemberDumpSchema as MemberDumpSchema
from .schemas import PublicDumpSchema as PublicDumpSchema
from .schemas import RequestMembershipSchema as RequestMembershipSchema
from .schemas import UpdateBulkSchema as UpdateBulkSchema

def invite_expires_at() -> datetime: ...

class MemberService(RecordService):
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
        scan: bool = ...,
        scan_params: None = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def _update(
        self,
        identity: Identity,
        community: Community,
        member: Member,
        role: Optional[Role],
        visible: Optional[bool],
        uow: UnitOfWork,
    ) -> None: ...
    def accept_invite(
        self, identity: Identity, request_id: str, uow: Optional[UnitOfWork] = ...
    ) -> None: ...
    def add(
        self,
        identity: Identity,
        community_id: str,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> bool: ...
    @property
    def add_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def archive_indexer(self) -> RecordIndexer: ...
    def close_membership_request(
        self, identity: Identity, request_id: str, uow: Optional[UnitOfWork] = ...
    ) -> None: ...
    @property
    def community_cls(self) -> Type[Community]: ...
    def decline_invite(
        self, identity: Identity, request_id: str, uow: Optional[UnitOfWork] = ...
    ) -> None: ...
    def members_delete(
        self,
        identity: Identity,
        community_id: str,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> None: ...
    @property
    def delete_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def invitation_dump_schema(self) -> ServiceSchemaWrapper: ...
    def invite(
        self,
        identity: Identity,
        community_id: str,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> bool: ...
    @property
    def invite_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def member_dump_schema(self) -> ServiceSchemaWrapper: ...
    @property
    def public_dump_schema(self) -> ServiceSchemaWrapper: ...
    def read_memberships(self, identity: Identity) -> Dict[str, Any]: ...
    def request_membership(
        self,
        identity: Identity,
        community_id: str,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
    ) -> RequestItem: ...
    @property
    def request_membership_schema(self) -> ServiceSchemaWrapper: ...
    def members_scan(
        self,
        identity: Identity,
        community_id: str,
        params: None = ...,
        search_preference: None = ...,
        extra_filter: Optional[Terms] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def members_search(
        self,
        identity: Identity,
        community_id: str,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        extra_filter: None = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def search_invitations(
        self,
        identity: Identity,
        community_id: str,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def search_public(
        self,
        identity: Identity,
        community_id: str,
        params: Optional[Dict[str, Any]] = ...,
        search_preference: Optional[str] = ...,
        **kwargs: Any,
    ) -> RecordList: ...
    def members_update(
        self,
        identity: Identity,
        community_id: str,
        data: Dict[str, Any],
        uow: Optional[UnitOfWork] = ...,
        refresh: bool = ...,
    ) -> None: ...
    @property
    def update_schema(self) -> ServiceSchemaWrapper: ...
    def update_membership_request(
        self, identity, community_id, data, uow=None
    ) -> None: ...
    def search_membership_requests(self) -> None: ...
    def accept_membership_request(self, identity, request_id, uow=None) -> None: ...
