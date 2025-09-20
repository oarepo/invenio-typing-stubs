from invenio_records_resources.services.files.transfer.base import Transfer

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
    ) -> Transfer: ...
    def get_transfer_class(self, transfer_type: str) -> Transfer: ...
    def register(
        self,
        transfer_cls: Transfer,
    ): ...
