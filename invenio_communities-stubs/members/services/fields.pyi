from typing import Any, Mapping, Optional

from invenio_communities.roles import Role
from marshmallow import fields

from ...proxies import current_roles as current_roles

class RoleField(fields.Str):
    default_error_messages: dict[str, str]
    roles: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _deserialize(
        self,
        value: str,
        attr: Optional[str],
        data: Optional[Mapping[str, Any]],
        **kwargs,
    ) -> Role: ...
