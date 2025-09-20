from typing import Any, Dict, List, Optional

from flask_principal import Identity
from invenio_records_resources.records.api import Record

from ..errors import InvalidMemberError as InvalidMemberError
from .models import ArchivedInvitationModel as ArchivedInvitationModel
from .models import MemberModel as MemberModel

relations_dumper: Any

class MemberMixin:
    community_id: Any
    user_id: Any
    group_id: Any
    request_id: Any
    role: Any
    visible: Any
    active: Any
    relations: Any
    @classmethod
    def get_memberships_from_group_ids(
        cls, identity: Identity, group_ids: List[Any]
    ) -> List[Any]: ...
    @classmethod
    def get_memberships(cls, identity: Identity) -> List[Any]: ...
    @classmethod
    def get_member_by_request(cls, request_id: str) -> Member: ...
    @classmethod
    def get_members(
        cls, community_id: str, members: Optional[List[Dict[str, Any]]] = None
    ) -> List[Any]: ...
    @classmethod
    def has_members(cls, community_id: str, role: Optional[str] = None) -> int: ...

class Member(Record, MemberMixin):
    model_cls = MemberModel
    dumper = relations_dumper
    metadata: None
    index: Any

class ArchivedInvitation(Record, MemberMixin):
    model_cls = ArchivedInvitationModel
    dumper = relations_dumper
    metadata: None
    index: Any
    @classmethod
    def create_from_member(cls, member: Member) -> ArchivedInvitation: ...
