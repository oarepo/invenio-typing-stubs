from typing import Any

from invenio_pidstore.models import PersistentIdentifier

from .base import PIDProvider

class OAIPIDProvider(PIDProvider):
    name: str

    def __init__(self, name: str, **kwargs: Any) -> None: ...
    def generate_id(self, record: Any, **kwargs: Any) -> str: ...
    @classmethod
    def is_enabled(cls, app: Any | None = ...) -> bool: ...
    def reserve(
        self, pid: PersistentIdentifier, record: Any | None = ..., **kwargs: Any
    ) -> bool: ...
