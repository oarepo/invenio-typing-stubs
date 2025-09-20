from collections.abc import ValuesView
from io import BufferedReader
from typing import (
    Any,
    Dict,
    Optional,
)

from flask.wrappers import Response
from flask_principal import (
    Identity,
)
from invenio_records_resources.records.api import (
    FileRecord,
    Record,
)
from invenio_records_resources.services.base.links import LinksTemplate
from invenio_records_resources.services.files.service import FileService

class FileItem:
    def __init__(
        self,
        service: FileService,
        identity: Identity,
        file_: FileRecord,
        record: Record,
        errors: None = ...,
        links_tpl: Optional[LinksTemplate] = ...,
    ): ...
    @property
    def _obj(self) -> FileRecord: ...
    @property
    def file_id(self) -> str: ...
    def get_stream(self, mode: str) -> BufferedReader: ...
    @property
    def links(self) -> Dict[str, Any]: ...
    def send_file(
        self, restricted: bool = ..., as_attachment: bool = ...
    ) -> Response: ...

class FileList:
    def __init__(
        self,
        service: FileService,
        identity: Identity,
        results: ValuesView,
        record: Record,
        links_tpl: Optional[LinksTemplate] = ...,
        links_item_tpl: Optional[LinksTemplate] = ...,
    ): ...
    @property
    def entries(self): ...
    def to_dict(self) -> Dict[str, Any]: ...
