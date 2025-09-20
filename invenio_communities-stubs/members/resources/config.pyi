from typing import Any

from invenio_records_resources.resources import RecordResourceConfig

from ...errors import CommunityDeletedError as CommunityDeletedError
from ..errors import AlreadyMemberError as AlreadyMemberError
from ..errors import InvalidMemberError as InvalidMemberError

class MemberResourceConfig(RecordResourceConfig):
    blueprint_name: str
    url_prefix: str
    routes: dict[str, str]
    request_view_args: dict[str, Any]
    error_handlers: dict[type, Any]
    response_handlers: dict[str, Any]
