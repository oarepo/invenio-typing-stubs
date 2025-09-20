from invenio_records_permissions.generators import Generator

class IfTransferType:
    def __init__(
        self, transfer_type: str, then_: Generator, else_: Generator | None = None
    ): ...
    def _condition(self, **kwargs) -> bool: ...
