"""Invenio module that stores and registers persistent identifiers.

Type stubs for invenio_pidstore.ext.
"""

from typing import Any, Callable, Dict, Optional

from flask import Flask

def pid_exists(value: str, pidtype: Optional[str] = None) -> bool: ...

class _PIDStoreState:
    """Persistent identifier store state."""

    app: Flask
    minters: Dict[str, Callable[..., Any]]
    fetchers: Dict[str, Callable[..., Any]]

    def __init__(
        self,
        app: Flask,
        minters_entry_point_group: Optional[str] = None,
        fetchers_entry_point_group: Optional[str] = None,
    ) -> None: ...
    def register_minter(self, name: str, minter: Callable[..., Any]) -> None: ...
    def register_fetcher(self, name: str, fetcher: Callable[..., Any]) -> None: ...
    def load_minters_entry_point_group(self, entry_point_group: str) -> None: ...
    def load_fetchers_entry_point_group(self, entry_point_group: str) -> None: ...

class InvenioPIDStore:
    """Invenio-PIDStore extension."""

    _state: _PIDStoreState

    def __init__(
        self,
        app: Optional[Flask] = None,
        minters_entry_point_group: str = "invenio_pidstore.minters",
        fetchers_entry_point_group: str = "invenio_pidstore.fetchers",
    ) -> None: ...
    def init_app(
        self,
        app: Flask,
        minters_entry_point_group: Optional[str] = None,
        fetchers_entry_point_group: Optional[str] = None,
    ) -> _PIDStoreState: ...
    def init_config(self, app: Flask) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
