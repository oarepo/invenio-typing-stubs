"""Internal resolver for persistent identifiers.

Type stubs for invenio_pidstore.resolver.
"""

from typing import Any, Callable, Optional, Tuple, Union

from invenio_pidstore.models import PersistentIdentifier

class Resolver:
    """Persistent identifier resolver."""

    pid_type: Optional[str]
    object_type: Optional[str]
    object_getter: Optional[Callable[[Any], Any]]
    registered_only: bool

    def __init__(
        self,
        pid_type: Optional[str] = None,
        object_type: Optional[str] = None,
        getter: Optional[Callable[[Any], Any]] = None,
        registered_only: bool = True,
    ) -> None: ...
    def resolve(
        self, pid_value: Union[str, int]
    ) -> Tuple[PersistentIdentifier, Any]: ...
