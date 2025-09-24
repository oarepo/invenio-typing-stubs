from __future__ import annotations

from marshmallow import Schema

class RecordSchema(Schema):
    id: Any

class CommunityRecordsSchema(Schema):
    records: Any
    def validate_records(self, value): ...
