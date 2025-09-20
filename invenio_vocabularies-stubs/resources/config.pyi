from typing import Any, Dict, Type

import marshmallow as ma
from flask_resources import HTTPJSONException as HTTPJSONException
from flask_resources import ResourceConfig
from flask_resources import create_error_handler as create_error_handler
from invenio_records_resources.resources import RecordResource as RecordResource
from invenio_records_resources.resources import RecordResourceConfig
from invenio_records_resources.resources.records.args import SearchRequestArgsSchema
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_vocabularies.resources.serializer import (
    VocabularyL10NItemSchema as VocabularyL10NItemSchema,
)

class VocabularySearchRequestArgsSchema(SearchRequestArgsSchema):
    tags: ma.fields.Str
    active: ma.fields.Boolean
    status: ma.fields.Boolean

class VocabulariesResourceConfig(RecordResourceConfig):
    blueprint_name: str | None
    url_prefix: str
    routes: Dict[str, str]
    request_view_args: Dict[str, ma.fields.Field]
    request_search_args = VocabularySearchRequestArgsSchema
    response_handlers: Dict[str, Any]

class VocabularyTypeResourceConfig(ResourceConfig, ConfiguratorMixin):
    blueprint_name: str | None
    url_prefix: str
    routes: Dict[str, str]
    request_read_args: Dict[str, Any]
    request_view_args: Dict[str, ma.fields.Field]
    request_search_args = VocabularySearchRequestArgsSchema
    error_handlers: Dict[Type[Exception], Any]
    response_handlers: Dict[str, Any]
