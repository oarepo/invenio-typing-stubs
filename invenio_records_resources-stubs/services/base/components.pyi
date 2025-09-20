from invenio_records_resources.services.files.service import FileService
from invenio_records_resources.services.records.service import RecordService
from typing import Union


class BaseServiceComponent:
    def __init__(
        self,
        service: Union[RecordService, FileService]
    ): ...
