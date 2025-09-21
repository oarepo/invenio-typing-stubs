from typing import (
    Dict,
    Union,
)

from werkzeug.wsgi import LimitedStream

class RequestStreamParser:
    def parse(self) -> Dict[str, Union[LimitedStream, int]]: ...
