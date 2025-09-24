from __future__ import annotations

from marshmallow import Schema

def validate_scheme(scheme) -> None: ...

class InternalNoteSchema(Schema):
    id: Any
    timestamp: Any
    added_by: Any
    note: Any

    class Meta:
        unknown: Any

class RDMRecordSchema(Schema):
    pids: Any
    metadata: Any
    custom_fields: Any
    access: Any
    files: Any
    media_files: Any
    revision: Any
    versions: Any
    parent: Any
    is_published: Any
    status: Any
    tombstone: Any
    deletion_status: Any
    internal_notes: Any
    stats: Any
    field_dump_permissions: dict[str, str]
    field_load_permissions: dict[str, str]

    class Meta:
        unknown: Any

    def default_nested(self, data): ...
    def hide_tombstone(self, data): ...
    def post_dump(self, data, many, **kwargs): ...
