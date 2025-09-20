from celery import shared_task
from invenio_requests.proxies import (
    current_requests_service as current_requests_service,
)
from invenio_requests.proxies import (
    current_user_moderation_service as current_user_moderation_service,
)
from invenio_requests.services.user_moderation.errors import (
    OpenRequestAlreadyExists as OpenRequestAlreadyExists,
)

@shared_task
def check_expired_requests() -> None: ...
def request_moderation(user_id: str) -> None: ...
