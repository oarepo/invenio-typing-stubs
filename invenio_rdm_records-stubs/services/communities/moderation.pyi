from typing import Any

from flask_principal import Identity
from invenio_records_resources.services.records.components import ServiceComponent

class BaseHandler:
    def create(
        self,
        identity: Identity,
        record: Any | None = ...,
        data: dict[str, Any] | None = ...,
        uow: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def update(
        self,
        identity: Identity,
        record: Any | None = ...,
        data: dict[str, Any] | None = ...,
        uow: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def delete(
        self,
        identity: Identity,
        data: dict[str, Any] | None = ...,
        record: Any | None = ...,
        uow: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...

class UserModerationHandler(BaseHandler):
    @property
    def enabled(self) -> bool: ...
    def run(
        self, identity: Identity, record: Any | None = ..., uow: Any | None = ...
    ) -> None: ...
    def create(
        self,
        identity: Identity,
        record: Any | None = ...,
        data: dict[str, Any] | None = ...,
        uow: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def update(
        self,
        identity: Identity,
        record: Any | None = ...,
        data: dict[str, Any] | None = ...,
        uow: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...

class ContentModerationComponent(ServiceComponent):
    def create(
        self,
        identity: Identity,
        record: Any | None = ...,
        data: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def update(
        self,
        identity: Identity,
        record: Any | None = ...,
        data: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def delete(
        self,
        identity: Identity,
        record: Any | None = ...,
        data: dict[str, Any] | None = ...,
        **kwargs: Any,
    ) -> None: ...
