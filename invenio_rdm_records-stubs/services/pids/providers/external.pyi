from typing import Any, Optional, Sequence

from invenio_pidstore.models import PersistentIdentifier

from .base import PIDProvider

class BlockedPrefixes:
    def __init__(
        self,
        prefixes: Optional[Sequence[str]] = ...,
        config_names: Optional[Sequence[str]] = ...,
    ) -> None: ...
    @property
    def prefixes(self) -> list[str]: ...
    def __call__(
        self, record: Any, identifier: str, provider: str, errors: list[str]
    ) -> None: ...

class ExternalPIDProvider(PIDProvider):
    def __init__(
        self,
        name: str,
        pid_type: str,
        validators: Optional[Sequence[BlockedPrefixes]] = ...,
        **kwargs: Any,
    ) -> None: ...
    @classmethod
    def is_enabled(cls, app: Any | None = ...) -> Any: ...
    def validate(
        self,
        record: Any,
        identifier: Optional[str] = ...,
        provider: Optional[str] = ...,
        client: Any | None = ...,
        **kwargs: Any,
    ) -> tuple[bool, list[dict[str, Any]]]: ...
    def delete(
        self, pid: PersistentIdentifier, soft_delete: bool = ..., **kwargs: Any
    ) -> bool: ...
