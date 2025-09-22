from typing import Callable

from flask import Response
from flask_resources import HTTPJSONException
from invenio_records_resources.services.errors import ValidationErrorGroup
from marshmallow import ValidationError

def create_pid_redirected_error_handler() -> Callable[[Exception], Response]: ...

class HTTPJSONValidationException(HTTPJSONException):
    def __init__(self, exception: ValidationError | ValidationErrorGroup) -> None: ...

class HTTPJSONSearchRequestError(HTTPJSONException):
    causes_responses: dict[str, tuple[int, str]]

    def __init__(self, error: Exception) -> None: ...

class ErrorHandlersMixin:
    error_handlers: dict[type[BaseException], Callable[[BaseException], Response]]
