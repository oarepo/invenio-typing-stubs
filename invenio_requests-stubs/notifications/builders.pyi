from typing import Sequence

from invenio_notifications.models import Notification
from invenio_notifications.services.builders import NotificationBuilder
from invenio_notifications.services.filters import RecipientFilter
from invenio_notifications.services.generators import (
    ContextGenerator,
    RecipientBackendGenerator,
    RecipientGenerator,
)

class CommentRequestEventCreateNotificationBuilder(NotificationBuilder):
    type: str
    context: Sequence[ContextGenerator]
    recipients: Sequence[RecipientGenerator]
    recipient_filters: Sequence[RecipientFilter]
    recipient_backends: Sequence[RecipientBackendGenerator]

    @classmethod
    def build(cls, **kwargs: object) -> Notification: ...
