from typing import (
    Callable,
)

from opensearchpy.exceptions import RequestError

def create_pid_redirected_error_handler() -> Callable: ...

class HTTPJSONSearchRequestError:
    def __init__(self, error: RequestError): ...

class HTTPJSONValidationException:
    def __init__(self, exception: Exception): ...
