from __future__ import annotations

from marshmallow import Schema

class EmbargoSchema(Schema):
    active: Any
    until: Any
    reason: Any
    def validate_embargo(self, data, **kwargs): ...

class AccessSchema(Schema):
    record: Any
    files: Any
    embargo: Any
    status: Any
    def validate_protection_value(self, value, field_name): ...
    def get_attribute(self, obj, attr, default): ...
    def validate_record_protection(self, value, data_key=None): ...
    def validate_files_protection(self, value, data_key=None): ...
