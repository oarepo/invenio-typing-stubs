from typing import Type, Union

from invenio_records_resources.services.files.transfer.providers.fetch import (
    FetchTransfer,
)
from invenio_records_resources.services.files.transfer.providers.local import (
    LocalTransfer,
)
from invenio_records_resources.services.files.transfer.providers.multipart import (
    MultipartTransfer,
)
from invenio_records_resources.services.files.transfer.providers.remote import (
    RemoteTransfer,
)

class TransferRegistry:
    def __init__(self, default_transfer_type: str): ...
    @property
    def default_transfer_type(self) -> str: ...
    def get_transfer(
        self,
        *,
        record,
        file_service,
        key=...,
        transfer_type=...,
        file_record=...,
        uow=...,
    ) -> Union[MultipartTransfer, RemoteTransfer, LocalTransfer, FetchTransfer]: ...
    def get_transfer_class(self, transfer_type: str) -> Union[
        Type[RemoteTransfer],
        Type[FetchTransfer],
        Type[LocalTransfer],
        Type[MultipartTransfer],
    ]: ...
    def register(
        self,
        transfer_cls: Union[
            Type[RemoteTransfer],
            Type[FetchTransfer],
            Type[LocalTransfer],
            Type[MultipartTransfer],
        ],
    ): ...
