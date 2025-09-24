from __future__ import annotations

from marshmallow import Schema

class QuotaSchema(Schema):
    quota_size: Any
    max_file_size: Any
    notes: Any
