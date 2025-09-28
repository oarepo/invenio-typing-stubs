from collections.abc import Callable, Mapping
from typing import Any, ClassVar

import marshmallow as ma
from flask import Response
from flask_resources import ResourceConfig
from flask_resources.responses import ResponseHandler
from invenio_records_resources.resources.records.args import SearchRequestArgsSchema
from invenio_records_resources.services.base.config import ConfiguratorMixin
from werkzeug.exceptions import HTTPException

oaipmh_error_handlers: dict[
    int | type[HTTPException] | type[BaseException],
    Callable[[Exception], Response],
]

class OAIPMHServerSearchRequestArgsSchema(SearchRequestArgsSchema):
    managed: ClassVar[ma.fields.Boolean]
    sort_direction: ClassVar[ma.fields.Str]

class OAIPMHServerResourceConfig(ResourceConfig, ConfiguratorMixin):
    blueprint_name: ClassVar[str | None]
    url_prefix: ClassVar[str | None]
    routes: ClassVar[dict[str, str]]

    request_read_args: ClassVar[dict[str, Any]]
    request_view_args: ClassVar[dict[str, ma.fields.Field]]
    request_search_args: ClassVar[
        type[SearchRequestArgsSchema] | type[OAIPMHServerSearchRequestArgsSchema]
    ]

    error_handlers: ClassVar[
        dict[
            int | type[HTTPException] | type[BaseException],
            Callable[[Exception], Response],
        ]
    ]

    response_handlers: ClassVar[Mapping[str, ResponseHandler]]
