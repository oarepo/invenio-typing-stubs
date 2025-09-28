from __future__ import annotations

from collections.abc import Callable, Mapping
from types import TracebackType
from typing import TYPE_CHECKING, Any, Protocol

from flask import Response
from werkzeug.local import LocalProxy

if TYPE_CHECKING:
    # mypy does not understand LocalProxy[ABC], so this is a workaround
    resource_requestctx: "ResourceRequestCtx"  # type: ignore

class ResponseHandlerProtocol(Protocol):
    def make_response(
        self, obj_or_list: Any, code: int, many: bool = False
    ) -> Response: ...

class ResourceConfigProtocol(Protocol):
    blueprint_name: str | None
    url_prefix: str | None
    error_handlers: Mapping[Any, Callable[[Exception], Response]]
    request_body_parsers: Mapping[str, Any]
    default_content_type: str | None
    response_handlers: Mapping[str, ResponseHandlerProtocol]
    default_accept_mimetype: str | None

class ResourceRequestCtx:
    config: ResourceConfigProtocol
    args: Mapping[str, Any] | None
    headers: Mapping[str, str] | None
    data: Any
    view_args: Mapping[str, Any] | None
    accept_mimetype: str | None
    response_handler: ResponseHandlerProtocol | None

    def __init__(self, config: ResourceConfigProtocol) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def update(self, values: Mapping[str, Any]) -> None: ...

def _get_context() -> ResourceRequestCtx: ...

resource_requestctx: LocalProxy[ResourceRequestCtx]  # type: ignore
