from typing import Any

from flask_principal import Identity
from invenio_drafts_resources.services.records.components import ServiceComponent

class MetadataComponent(ServiceComponent):
    field: str
    new_version_skip_fields: list[str]
    def create(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def update_draft(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        errors: Any | None = ...,
    ) -> None: ...
    def publish(
        self,
        identity: Identity,
        draft: Any | None = ...,
        record: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def edit(
        self,
        identity: Identity,
        draft: Any | None = ...,
        record: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def new_version(
        self,
        identity: Identity,
        draft: Any | None = ...,
        record: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
