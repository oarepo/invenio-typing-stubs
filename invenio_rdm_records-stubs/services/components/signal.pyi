from typing import Any

from flask_principal import Identity
from invenio_drafts_resources.services.records.components import ServiceComponent

class SignalComponent(ServiceComponent):
    """Service component to trigger signals on publish."""

    def publish(
        self, identity: Identity, draft: Any | None = ..., record: Any | None = ...
    ) -> None: ...
