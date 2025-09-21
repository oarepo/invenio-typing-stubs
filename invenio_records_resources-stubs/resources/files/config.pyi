from typing import Callable, Dict

from flask_resources import ResourceConfig  # type: ignore[import-untyped]

class FileResourceConfig(ResourceConfig):
    """File resource config."""

    blueprint_name: str | None = None
    url_prefix: str
    routes: Dict[str, str]
    error_handlers: dict[Exception, Callable]
    # Optional toggles that may be used (fallback to service config in source)
    allow_upload: bool | None
    allow_archive_download: bool | None
