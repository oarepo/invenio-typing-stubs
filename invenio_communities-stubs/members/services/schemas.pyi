from typing import Dict, List, Optional, Union

from invenio_communities.members.records.api import Member
from invenio_communities.roles import Role
from marshmallow import Schema, fields, validates_schema

from .fields import RoleField as RoleField

class MemberEntitySchema(Schema):
    type: fields.Str
    id: fields.Str
    is_current_user: fields.Bool

class MembersSchema(Schema):
    members: fields.List

class RequestSchema(Schema):
    id: fields.Str
    status: fields.Str
    is_open: fields.Bool
    expires_at: fields.Str

class AddBulkSchema(MembersSchema, Schema):
    role: RoleField
    visible: fields.Bool

class InviteBulkSchema(AddBulkSchema):
    message: fields.Str

class UpdateBulkSchema(MembersSchema, Schema):
    role: RoleField
    visible: fields.Bool
    @validates_schema
    def validate_schema(
        self, data: Dict[str, Union[List[Dict[str, str]], Role, bool]], **kwargs
    ) -> None: ...

class DeleteBulkSchema(MembersSchema): ...

class RequestMembershipSchema(Schema):
    message: fields.Str

class PublicDumpSchema(Schema):
    id: fields.Str
    member: fields.Method
    def get_member(self, obj: Member) -> Dict[str, str]: ...
    def get_user_member(
        self,
        user: Dict[
            str,
            Optional[
                Union[str, Dict[str, str], Dict[str, Union[str, Dict[str, bool]]], bool]
            ],
        ],
    ) -> Dict[str, str]: ...
    def get_group_member(self, group: Dict[str, str]) -> Dict[str, str]: ...

class MemberDumpSchema(PublicDumpSchema):
    role: fields.Str
    visible: fields.Bool
    is_current_user: fields.Method
    permissions: fields.Method
    created: fields.DateTime
    updated: fields.DateTime
    revision_id: fields.Int
    def is_self(self, obj: Member) -> bool: ...
    def get_current_user(self, obj: Member) -> bool: ...
    def get_permissions(self, obj: Member) -> Dict[str, bool]: ...

class InvitationDumpSchema(MemberDumpSchema):
    request: fields.Nested
    permissions: fields.Method
    def get_permissions(self, obj: Member) -> Dict[str, bool]: ...
