from __future__ import annotations

from marshmallow import Schema

class MetadataSchema(Schema):
    page: Any
    type: Any
    language: Any
    encoding: Any
    charset: Any
    previewer: Any
    width: Any
    height: Any

class AccessSchema(Schema):
    hidden: Any

class ProcessorSchema(Schema):
    type: Any
    status: Any
    source_file_id: Any
    props: Any

class FileSchema(Schema):
    id: Any
    checksum: Any
    ext: Any
    size: Any
    mimetype: Any
    storage_class: Any
    key: Any
    metadata: Any
    access: Any
    processor: Any

class FilesSchema(Schema):
    field_dump_permissions: dict[str, str]
    enabled: Any
    default_preview: Any
    order: Any
    count: Any
    total_bytes: Any
    entries: Any
    def clean(self, data, **kwargs): ...
    def get_attribute(self, obj, attr, default): ...

class MediaFileSchema(FileSchema):
    language: Any
