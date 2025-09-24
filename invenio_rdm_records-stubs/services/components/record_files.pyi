from typing import Any

from flask_principal import Identity
from invenio_drafts_resources.services.records.components import ServiceComponent

class RecordFilesProcessorComponent(ServiceComponent):
    """Service component for RecordFilesProcessor."""

    def publish(
        self, identity: Identity, draft: Any | None = ..., record: Any | None = ...
    ) -> None: ...
    def lift_embargo(
        self, identity: Identity, draft: Any | None = ..., record: Any | None = ...
    ) -> None: ...
