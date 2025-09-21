import marshmallow as ma
from flask_resources import (  # type: ignore[import-untyped]
    RequestBodyParser,
    ResourceConfig,
    ResponseHandler,
)
from invenio_records_resources.resources.records.args import SearchRequestArgsSchema

class RecordResourceConfig(ResourceConfig):
    blueprint_name: str | None
    url_prefix: str
    routes: dict[str, str]
    request_read_args: dict[str, ma.fields.Field]
    request_view_args: dict[str, ma.fields.Field]
    request_search_args: type[SearchRequestArgsSchema]
    request_extra_args: dict[str, ma.fields.Field]
    request_headers: dict[str, ma.fields.Field]
    request_body_parsers: dict[str, RequestBodyParser]
    default_content_type: str

    # Response handling
    response_handlers: dict[str, ResponseHandler]
    default_accept_mimetype: str
