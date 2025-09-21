from typing import Any, Optional, Union

from invenio_records_resources.services.files.service import FileService
from invenio_records_resources.services.records.service import RecordService

class BaseServiceComponent:
    service: Union[RecordService, FileService]
    _uow: Any
    def __init__(self, service: Union[RecordService, FileService]): ...
    @property
    def uow(self) -> Any: ...
    @uow.setter
    def uow(self, value: Optional[Any]) -> None: ...
