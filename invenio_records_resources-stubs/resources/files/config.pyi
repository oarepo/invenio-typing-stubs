from typing import Callable, Dict

from flask_resources import ResourceConfig

class FileResourceConfig(ResourceConfig):
    """File resource config."""

    blueprint_name: str | None = None
    url_prefix: str
    routes: Dict[str, str]
    error_handlers: dict[Exception, Callable]
