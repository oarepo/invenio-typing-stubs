from _typeshed import Incomplete
from marshmallow import EXCLUDE, Schema, pre_dump, pre_load

class ResourceSchema(Schema):
    type: Incomplete
    id: Incomplete

class MetadataSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    ip_address: Incomplete
    session: Incomplete
    request_id: Incomplete
    parent_pid: Incomplete
    revision_id: Incomplete

class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id: Incomplete
    username: Incomplete
    email: Incomplete
    @pre_load
    def serialize_user(self, obj, **kwargs): ...

class AuditLogSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    id: Incomplete
    created: Incomplete
    action: Incomplete
    resource: Incomplete
    metadata: Incomplete
    user: Incomplete
    user_id: Incomplete
    resource_type: Incomplete
    @pre_dump
    def add_timestamp(self, obj, **kwargs): ...
