from typing import Any

from flask_principal import Identity
from invenio_drafts_resources.services.records.components import ServiceComponent

OPTIONAL_DOI_TRANSITIONS: dict[str, dict[str, Any]]

def validate_optional_doi(
    draft: Any,
    previous_published_record: Any,
    errors: list[dict[str, Any]] | None = ...,
    transitions_config: dict[str, dict[str, Any]] | None = ...,
) -> dict[str, Any]: ...

class PIDsComponent(ServiceComponent):
    """Service component for PIDs."""

    def _validate_optional_doi(self, *args: Any, **kwargs: Any) -> Any: ...
    def _find_changed_pids_to_discard_from_source(
        self, source_pids: dict[str, Any], dest_pids: dict[str, Any]
    ) -> dict[str, Any]: ...
    def create(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        errors: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def update_draft(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        errors: Any | None = ...,
    ) -> None: ...
    def delete_draft(
        self,
        identity: Identity,
        draft: Any | None = ...,
        record: Any | None = ...,
        force: bool = ...,
    ) -> None: ...
    def publish(
        self, identity: Identity, draft: Any | None = ..., record: Any | None = ...
    ) -> None: ...
    def new_version(
        self, identity: Identity, draft: Any | None = ..., record: Any | None = ...
    ) -> None: ...
    def edit(
        self, identity: Identity, draft: Any | None = ..., record: Any | None = ...
    ) -> None: ...
    def delete_record(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        uow: Any | None = ...,
    ) -> None: ...
    def restore_record(
        self, identity: Identity, record: Any | None = ..., uow: Any | None = ...
    ) -> None: ...

class ParentPIDsComponent(ServiceComponent):
    """Service component for record parent PIDs."""

    def create(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        errors: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def publish(
        self, identity: Identity, draft: Any | None = ..., record: Any | None = ...
    ) -> None: ...
    def delete_record(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        uow: Any | None = ...,
    ) -> None: ...
    def restore_record(
        self, identity: Identity, record: Any | None = ..., uow: Any | None = ...
    ) -> None: ...
