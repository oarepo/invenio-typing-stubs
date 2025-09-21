from typing import Any, Callable, Dict, Type

from flask_resources import HTTPJSONException
from opensearchpy.exceptions import RequestError

# Imported in implementation to build handlers; not referenced directly in stubs.
# from invenio_records_resources.services.errors import (...)

def create_pid_redirected_error_handler() -> Callable[[Exception], Any]: ...

class HTTPJSONValidationException(HTTPJSONException):
    description: str | None

    def __init__(self, exception: Exception) -> None: ...

class HTTPJSONSearchRequestError(HTTPJSONException):
    causes_responses: Dict[str, tuple[int, str]]

    def __init__(self, error: RequestError) -> None: ...

class ErrorHandlersMixin:
    error_handlers: Dict[Type[BaseException], Callable[..., HTTPJSONException]]
