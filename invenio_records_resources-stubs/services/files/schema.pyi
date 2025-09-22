from typing import (
    Any,
    Dict,
)

import marshmallow as ma
from invenio_records_resources.records.api import FileRecord
from marshmallow import Schema

class BaseTransferSchema(Schema): ...

class TransferTypeSchemas:
    def __getitem__(self, transfer_type: str) -> ma.Schema: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class TransferSchema:
    def get_obj_type(
        self,
        obj: Any,
    ) -> str: ...

class FileAccessSchema(Schema): ...

class FileSchema(Schema):
    def dump_file_fields(
        self, obj: Dict[str, Any], original: FileRecord, **kwargs
    ) -> Dict[str, Any]: ...
    def dump_status(self, obj: FileRecord) -> str: ...

class InitFileSchemaMixin(Schema):
    def _fill_initial_transfer(self, data: Any, **kwargs) -> Any: ...
