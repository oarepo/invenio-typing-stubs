from __future__ import annotations

from marshmallow import Schema

class AgentSchema(Schema):
    user: Any

class RemovalReasonSchema(Schema):
    id: Any

class TombstoneSchema(Schema):
    removal_reason: Any
    note: Any
    removed_by: Any
    removal_date: Any
    citation_text: Any
    is_visible: Any

class DeletionStatusSchema(Schema):
    is_deleted: Any
    status: Any
