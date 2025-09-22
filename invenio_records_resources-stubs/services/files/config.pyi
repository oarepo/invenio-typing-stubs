from typing import Any, Type

from invenio_records_resources.services.base import ServiceConfig as ServiceConfig
from invenio_records_resources.services.files.components import (
    FileContentComponent as FileContentComponent,
)
from invenio_records_resources.services.files.components import (
    FileMetadataComponent as FileMetadataComponent,
)
from invenio_records_resources.services.files.components import (
    FileMultipartContentComponent as FileMultipartContentComponent,
)
from invenio_records_resources.services.files.components import (
    FileProcessorComponent as FileProcessorComponent,
)
from invenio_records_resources.services.files.processors import (
    FileProcessor,
)
from invenio_records_resources.services.files.processors import (
    ImageMetadataExtractor as ImageMetadataExtractor,
)
from invenio_records_resources.services.files.results import FileItem as FileItem
from invenio_records_resources.services.files.results import FileList as FileList
from invenio_records_resources.services.files.schema import FileSchema as FileSchema

class FileServiceConfig(ServiceConfig):
    service_id: str | None
    record_cls: type[Any] | None
    permission_action_prefix: str

    file_result_item_cls: Type[FileItem]
    file_result_list_cls: Type[FileList]
    file_schema: Type[FileSchema]

    max_files_count: int

    file_links_list: dict[str, Any]
    file_links_item: dict[str, Any]

    allow_upload: bool
    allow_archive_download: bool

    components: list[type[Any]]
    file_processors: list[FileProcessor]
