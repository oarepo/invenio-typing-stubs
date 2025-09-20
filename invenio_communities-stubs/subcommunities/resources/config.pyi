from typing import Any, Dict

from flask_resources import ResourceConfig, ResponseHandler
from invenio_communities.communities.resources.args import (
    CommunitiesSearchRequestArgsSchema as CommunitiesSearchRequestArgsSchema,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from marshmallow import fields

from ..services.errors import ParentChildrenNotAllowed as ParentChildrenNotAllowed

json_response_handler: ResponseHandler

class SubCommunityResourceConfig(ConfiguratorMixin, ResourceConfig):
    blueprint_name: str
    url_prefix: str
    routes: Dict[str, str]  # Route name to URL pattern mapping
    request_view_args: Dict[str, fields.Field]  # View argument field definitions
    request_read_args: Dict[str, Any]  # Read argument definitions
    request_extra_args: Dict[str, Any]  # Extra argument definitions
    request_body_parsers: Dict[str, Any]  # Body parser mappings
    default_content_type: str
    request_search_args = CommunitiesSearchRequestArgsSchema
    response_handlers: Dict[str, ResponseHandler]  # Content type to handler mapping
    default_accept_mimetype: str
    error_handlers: Dict[type, Any]  # Exception type to handler mapping
