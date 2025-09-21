"""DataCite PID provider.

Type stubs for invenio_pidstore.providers.datacite.
"""

from typing import Any, ClassVar, Optional

from invenio_pidstore.models import PIDStatus
from invenio_pidstore.providers.base import BaseProvider

class DataCiteProvider(BaseProvider):
    """DOI provider using DataCite API."""

    pid_type: ClassVar[str]  # type: ignore[assignment]
    pid_provider: ClassVar[str]  # type: ignore[assignment]
    default_status: ClassVar[PIDStatus]
    api: Any

    def __init__(
        self,
        pid: Any,
        client: Optional[Any] = None,
        **kwargs: Any,
    ) -> None: ...
    def reserve(self, doc: str) -> bool: ...
    def register(self, url: str, doc: str) -> bool: ...
    def update(self, url: str, doc: str) -> bool: ...
    def delete(self) -> bool: ...
    def sync_status(self) -> bool: ...
