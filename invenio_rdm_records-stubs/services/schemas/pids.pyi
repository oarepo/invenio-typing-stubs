from __future__ import annotations

from marshmallow import Schema

class PIDSchema(Schema):
    identifier: Any
    provider: Any
    client: Any
