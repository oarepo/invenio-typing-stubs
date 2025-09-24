from typing import Any

from flask_principal import Identity
from invenio_drafts_resources.services.records.components import ServiceComponent

class AccessComponent(ServiceComponent):
    def _populate_access_and_validate(
        self, identity: Identity, data: dict[str, Any], record: Any, **kwargs: Any
    ) -> None: ...
    def _init_owner(self, identity: Identity, record: Any, **kwargs: Any) -> None: ...
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
