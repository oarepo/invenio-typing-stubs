from typing import Any

from flask_principal import Identity
from invenio_drafts_resources.services.records.components import ServiceComponent

class ReviewComponent(ServiceComponent):
    """Service component for request integration."""

    def create(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def delete_draft(
        self,
        identity: Identity,
        draft: Any | None = ...,
        record: Any | None = ...,
        force: bool = ...,
    ) -> None: ...
    def publish(
        self,
        identity: Identity,
        draft: Any | None = ...,
        record: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
