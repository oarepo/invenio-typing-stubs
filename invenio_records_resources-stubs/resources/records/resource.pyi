from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Type,
    Union,
)

from invenio_records_resources.resources.records.config import RecordResourceConfig
from invenio_records_resources.services.records.service import RecordService

class RecordResource:
    def __init__(self, config: Type[RecordResourceConfig], service: RecordService): ...
    def create(self) -> Any: ...
    def create_url_rules(
        self,
    ) -> List[Dict[str, Optional[Union[str, List[str], Callable]]]]: ...
    def delete(self): ...
    def read(self) -> Any: ...
    def search(
        self,
    ) -> Any: ...
    def update(
        self,
    ) -> Any: ...

#
# Decorators
#
request_data: Callable[[Callable[..., Any]], Callable[..., Any]]
request_read_args: Callable[[Callable[..., Any]], Callable[..., Any]]
request_view_args: Callable[[Callable[..., Any]], Callable[..., Any]]
request_headers: Callable[[Callable[..., Any]], Callable[..., Any]]
request_search_args: Callable[[Callable[..., Any]], Callable[..., Any]]
request_extra_args: Callable[[Callable[..., Any]], Callable[..., Any]]
