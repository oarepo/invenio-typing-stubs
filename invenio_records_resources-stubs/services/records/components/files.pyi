from typing import Any

from invenio_records_resources.records.api import Record
from invenio_records_resources.services.base.service import Service
from invenio_records_resources.services.records.components.base import ServiceComponent

class FileConfigMixin:
    _files_attr_key: str | None = None
    _files_data_key: str | None = None
    _files_bucket_attr_key: str | None = None
    _files_bucket_id_attr_key: str | None = None

    @property
    def files_attr_key(self) -> str | None: ...
    @property
    def files_data_key(self) -> str | None: ...
    @property
    def files_bucket_attr_key(self) -> str | None: ...
    @property
    def files_bucket_id_attr_key(self) -> str | None: ...
    def get_record_files(self, record: Record) -> Any: ...  # FilesManager
    def get_record_bucket(self, record: Record) -> Any: ...  # Bucket
    def get_record_bucket_id(self, record: Record) -> str: ...

class BaseRecordFilesComponent(FileConfigMixin, ServiceComponent):
    def __init__(self, service: Service): ...
    def _validate_files_enabled(self, record: Record, enabled: bool) -> None: ...
    def assign_files_enabled(self, record: Record, enabled: bool) -> None: ...
    def assign_files_default_preview(
        self, record: Record, default_preview: bool
    ) -> None: ...

FilesAttrConfig: dict[str, Any]

FilesComponent: type[BaseRecordFilesComponent]
