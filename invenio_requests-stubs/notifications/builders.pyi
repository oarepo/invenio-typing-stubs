from typing import Any, List

from invenio_notifications.models import Notification
from invenio_requests.notifications.filters import (
    UserRecipientFilter as UserRecipientFilter,
)
from invenio_requests.notifications.generators import (
    RequestParticipantsRecipient as RequestParticipantsRecipient,
)
from invenio_requests.records.api import (
    Request,
    RequestEvent,
)

class CommentRequestEventCreateNotificationBuilder:
    type: str
    context: List[Any]  # EntityResolve generators
    recipients: List[Any]  # Recipient generators
    recipient_filters: List[Any]  # Recipient filters
    recipient_backends: List[Any]  # Backend processors

    @classmethod
    def build(cls, request: Request, request_event: RequestEvent) -> Notification: ...
