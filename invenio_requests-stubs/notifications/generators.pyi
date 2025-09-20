from typing import (
    Any,
    Dict,
    Optional,
)

from invenio_requests.proxies import current_events_service as current_events_service

class RequestParticipantsRecipient:
    key: str
    def __init__(self, key: str) -> None: ...
    def _get_user_id(self, request_field: Dict[str, Any]) -> Optional[str]: ...
    def __call__(
        self, notification: Any, recipients: Dict[str, Any]
    ) -> Dict[str, Any]: ...
