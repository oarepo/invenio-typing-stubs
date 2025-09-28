from collections.abc import Callable, Mapping
from typing import Any, ClassVar

import marshmallow as ma
from flask import Response
from flask_resources import RequestBodyParser, ResourceConfig, ResponseHandler
from invenio_communities.communities.resources.args import (
    CommunitiesSearchRequestArgsSchema as CommunitiesSearchRequestArgsSchema,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from werkzeug.exceptions import HTTPException

json_response_handler: ResponseHandler

class SubCommunityResourceConfig(ConfiguratorMixin, ResourceConfig):
    blueprint_name: ClassVar[str | None]
    url_prefix: ClassVar[str | None]
    routes: ClassVar[dict[str, str]]
    request_view_args: ClassVar[dict[str, ma.fields.Field]]
    request_read_args: ClassVar[dict[str, Any]]
    request_extra_args: ClassVar[dict[str, ma.fields.Field]]
    request_body_parsers: ClassVar[Mapping[str, RequestBodyParser]]
    default_content_type: ClassVar[str | None]
    request_search_args: ClassVar[type[CommunitiesSearchRequestArgsSchema]]
    response_handlers: ClassVar[Mapping[str, ResponseHandler]]
    default_accept_mimetype: ClassVar[str | None]
    error_handlers: ClassVar[
        dict[
            int | type[HTTPException] | type[BaseException],
            Callable[[Exception], Response],
        ]
    ]
