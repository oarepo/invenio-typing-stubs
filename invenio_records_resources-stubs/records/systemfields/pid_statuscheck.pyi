from typing import (
    Any,
    Dict,
    Optional,
)

from invenio_pidstore.models import PIDStatus
from invenio_records.systemfields import SystemField
from invenio_records_resources.records.api import (
    Record,
)

class PIDStatusCheckField[R: Record = Record](SystemField[R, bool]):
    def __init__(
        self, key: str = ..., status: Optional[PIDStatus] = ..., dump: bool = ...
    ) -> None: ...
    def pre_dump(
        self,
        data: Dict[Any, Any],
        **kwargs: Any,
    ) -> None: ...
    def pre_load(self, data: Dict[str, Any], **kwargs: Any) -> None: ...
