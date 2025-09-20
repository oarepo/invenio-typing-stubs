from io import (
    BufferedReader,
    BytesIO,
)
from typing import (
    Any,
    Dict,
    Optional,
    Type,
    Union,
)

from flask_principal import (
    Identity,
)
from invenio_db.uow import UnitOfWork
from invenio_records_resources.records.api import Record
from invenio_records_resources.services.base.links import LinksTemplate
from invenio_records_resources.services.files.results import (
    FileItem,
    FileList,
)
from invenio_records_resources.services.records.schema import ServiceSchemaWrapper
from werkzeug.wsgi import LimitedStream

class FileService:
    def _get_record(
        self,
        id_: str,
        identity: Identity,
        action: str,
        file_key: Optional[str] = ...,
    ) -> Record: ...
    def check_permission(
        self, identity: Identity, action_name: str, **kwargs
    ) -> bool: ...
    def commit_file(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        uow: Optional[UnitOfWork] = ...,
    ) -> FileItem: ...
    def delete_all_files(
        self, identity: Identity, id_: str, uow: Optional[UnitOfWork] = ...
    ) -> FileList: ...
    def delete_file(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        uow: Optional[UnitOfWork] = ...,
    ) -> FileItem: ...
    def extract_file_metadata(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        uow: Optional[UnitOfWork] = ...,
    ) -> FileItem: ...
    def file_links_item_tpl(self, id_: str) -> LinksTemplate: ...
    def file_links_list_tpl(self, id_: str) -> LinksTemplate: ...
    def file_result_item(self, *args, **kwargs) -> FileItem: ...
    def file_result_list(self, *args, **kwargs) -> FileList: ...
    @property
    def file_schema(self) -> ServiceSchemaWrapper: ...
    def get_file_content(
        self, identity: Identity, id_: str, file_key: str
    ) -> FileItem: ...
    def get_transfer_metadata(
        self, identity: Identity, id_: str, file_key: str
    ) -> Dict[str, str]: ...
    def init_files(
        self,
        identity: Identity,
        id_: str,
        data: Any,
        uow: Optional[UnitOfWork] = ...,
    ) -> FileList: ...
    @property
    def initial_file_schema(self) -> ServiceSchemaWrapper: ...
    def list_files(self, identity: Identity, id_: str) -> FileList: ...
    def read_file_metadata(
        self, identity: Identity, id_: str, file_key: str
    ) -> FileItem: ...
    @property
    def record_cls(self) -> Type[Record]: ...
    def set_file_content(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        stream: Union[BytesIO, BufferedReader, LimitedStream],
        content_length: Optional[int] = ...,
        uow: Optional[UnitOfWork] = ...,
    ) -> FileItem: ...
    def set_multipart_file_content(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        part: int,
        stream: Union[BytesIO, LimitedStream],
        content_length: Optional[int] = ...,
        uow: Optional[UnitOfWork] = ...,
    ) -> FileItem: ...
    def update_file_metadata(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        data: Dict[str, Dict[str, str]],
        uow: Optional[UnitOfWork] = ...,
    ) -> FileItem: ...
    def update_transfer_metadata(
        self,
        identity: Identity,
        id_: str,
        file_key: str,
        transfer_metadata: Dict[str, str],
        uow: Optional[UnitOfWork] = ...,
    ): ...
