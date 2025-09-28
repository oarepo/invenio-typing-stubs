from collections.abc import Callable
from typing import ClassVar

import marshmallow as ma
from flask import Response
from flask_resources import ResponseHandler
from invenio_communities.errors import CommunityDeletedError as CommunityDeletedError
from invenio_communities.members.errors import (
    AlreadyMemberError as AlreadyMemberError,
)
from invenio_communities.members.errors import (
    InvalidMemberError as InvalidMemberError,
)
from invenio_records_resources.resources import RecordResourceConfig
from werkzeug.exceptions import HTTPException

class MemberResourceConfig(RecordResourceConfig):
    url_prefix: ClassVar[str]
    routes: ClassVar[dict[str, str]]
    request_view_args: ClassVar[dict[str, ma.fields.Field]]
    # Mapping from exception type to an error handler (callable or factory)
    error_handlers: ClassVar[
        dict[
            int | type[HTTPException] | type[BaseException],
            Callable[[Exception], Response],
        ]
    ]
    response_handlers: ClassVar[dict[str, ResponseHandler]]
