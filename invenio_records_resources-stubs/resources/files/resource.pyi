from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Type,
    Union,
)

from flask.wrappers import Response
from invenio_records_resources.resources.files.config import FileResourceConfig
from invenio_records_resources.services.files.service import FileService

def set_max_content_length(func: Callable[..., Any]) -> Callable[..., Any]: ...

class FileResource:
    def __init__(self, config: Type[FileResourceConfig], service: FileService): ...
    def create(
        self,
    ) -> Any: ...
    def create_commit(
        self,
    ) -> Any: ...
    def create_url_rules(
        self,
    ) -> List[Dict[str, Optional[Union[str, List[str], Callable]]]]: ...
    def delete(self): ...
    def read(
        self,
    ) -> Any: ...
    def read_archive(self) -> Response: ...
    def read_content(self): ...
    def search(
        self,
    ) -> Any: ...
    def update(
        self,
    ) -> Any: ...
    def update_content(
        self,
    ) -> Any: ...
    def upload_multipart_content(self) -> Any: ...

# Decorators
request_view_args: Callable[[Callable[..., Any]], Callable[..., Any]]
request_data: Callable[[Callable[..., Any]], Callable[..., Any]]
request_stream: Callable[[Callable[..., Any]], Callable[..., Any]]
request_multipart_args: Callable[[Callable[..., Any]], Callable[..., Any]]
