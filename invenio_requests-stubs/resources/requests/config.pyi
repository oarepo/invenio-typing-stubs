from typing import Any, Dict, Optional

from _typeshed import Incomplete
from invenio_records_resources.resources import (
    RecordResourceConfig,
    SearchRequestArgsSchema,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_requests.errors import CannotExecuteActionError as CannotExecuteActionError
from invenio_requests.errors import NoSuchActionError as NoSuchActionError
from invenio_requests.resources.requests.fields import (
    ReferenceString as ReferenceString,
)
from marshmallow import fields

class RequestSearchRequestArgsSchema(SearchRequestArgsSchema):
    created_by: ReferenceString
    topic: ReferenceString
    receiver: ReferenceString
    is_open: fields.Boolean
    shared_with_me: fields.Boolean

request_error_handlers: Dict[type, Any]

class RequestsResourceConfig(RecordResourceConfig, ConfiguratorMixin):
    blueprint_name: Optional[str]
    url_prefix: str
    routes: Dict[str, str]
    request_view_args: Dict[str, Any]
    request_search_args = RequestSearchRequestArgsSchema
    error_handlers: Any
    response_handlers: Dict[str, Incomplete]
