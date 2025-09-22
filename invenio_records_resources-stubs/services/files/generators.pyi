from invenio_records_permissions.generators import ConditionalGenerator

class IfTransferType(ConditionalGenerator):
    def __init__(
        self,
        transfer_type: str,
        then_: ConditionalGenerator,
        else_: ConditionalGenerator | None = None,
    ): ...
    def _condition(self, **kwargs) -> bool: ...
