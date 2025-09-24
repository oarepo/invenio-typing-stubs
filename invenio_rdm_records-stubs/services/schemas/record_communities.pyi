from __future__ import annotations

from marshmallow import Schema

class CommunitySchema(Schema):
    id: Any
    comment: Any
    require_review: Any

class RecordCommunitiesSchema(Schema):
    communities: Any
    def validate_communities(self, value): ...
