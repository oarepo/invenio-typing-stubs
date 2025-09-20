from typing import Any, List, Optional, Union
from uuid import UUID

from flask_sqlalchemy.query import Query
from invenio_db import db
from invenio_records.models import RecordMetadataBase
from sqlalchemy.ext.declarative import declared_attr

from ...communities.records.models import CommunityMetadata as CommunityMetadata

class BaseMemberModel(RecordMetadataBase):
    id: Any
    @declared_attr
    def community_id(cls): ...
    role: Any
    visible: Any
    @declared_attr
    def user_id(cls): ...
    @declared_attr
    def group_id(cls): ...
    @declared_attr
    def request_id(cls): ...
    active: Any
    @classmethod
    def query_memberships(
        cls,
        user_id: Optional[int] = None,
        group_ids: Optional[List[Union[Any, str]]] = None,
        active: bool = True,
    ) -> Query: ...
    @classmethod
    def count_members(
        cls, community_id: UUID, role: Optional[str] = None, active: bool = True
    ) -> int: ...

class MemberModel(db.Model, BaseMemberModel):
    __tablename__: str
    __table_args__: tuple[Any, ...]

class ArchivedInvitationModel(db.Model, BaseMemberModel):
    __tablename__: str
    @classmethod
    def from_member_model(
        cls, member_model: MemberModel
    ) -> ArchivedInvitationModel: ...
