from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, ClassVar

from flask import Blueprint, Response
from flask_resources.config import ConfigAttrValue
from flask_resources.parsers import RequestBodyParser
from flask_resources.responses import ResponseHandler, ResponseTuple
from werkzeug.exceptions import HTTPException

ViewCallable = Callable[..., Response | ResponseTuple]
Decorator = Callable[[ViewCallable], ViewCallable]

def route(
    method: str,
    rule: str | ConfigAttrValue[Any],
    view_meth: ViewCallable,
    endpoint: str | None = ...,
    rule_options: Mapping[str, Any] | None = ...,
    apply_decorators: bool = ...,
) -> dict[str, Any]: ...

class ResourceConfig:
    blueprint_name: ClassVar[str | None]
    url_prefix: ClassVar[str | None]
    error_handlers: ClassVar[
        dict[
            int | type[HTTPException] | type[BaseException],
            Callable[[Exception], Response],
        ]
    ]
    request_body_parsers: ClassVar[Mapping[str, RequestBodyParser]]
    default_content_type: ClassVar[str | None]
    response_handlers: ClassVar[Mapping[str, ResponseHandler]]
    default_accept_mimetype: ClassVar[str | None]

class Resource:
    config: ResourceConfig
    decorators: ClassVar[Sequence[Decorator]]
    error_handlers: ClassVar[
        dict[
            int | type[HTTPException] | type[BaseException],
            Callable[[Exception], Response],
        ]
    ]

    def __init__(self, config: ResourceConfig) -> None: ...
    def as_blueprint(self, **options: Any) -> Blueprint: ...
    def create_blueprint(self, **options: Any) -> Blueprint: ...
    def create_url_rules(self) -> Sequence[dict[str, Any]]: ...
    def create_error_handlers(
        self,
    ) -> Iterable[
        tuple[
            int | type[HTTPException] | type[BaseException],
            Callable[[Exception], Response],
        ]
    ]: ...
