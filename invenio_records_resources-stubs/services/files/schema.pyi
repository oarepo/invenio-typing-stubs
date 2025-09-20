from typing import (
    Any,
    Dict,
)

import marshmallow as ma
from invenio_records_resources.records.api import FileRecord

class FileSchema:
    def dump_file_fields(
        self, obj: Dict[str, Any], original: FileRecord, **kwargs
    ) -> Dict[str, Any]: ...
    def dump_status(self, obj: FileRecord) -> str: ...

class TransferSchema:
    def get_obj_type(
        self,
        obj: Any,
    ) -> str: ...

class TransferTypeSchemas:
    def __getitem__(self, transfer_type: str) -> ma.Schema: ...
