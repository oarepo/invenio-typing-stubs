from typing import (
    Any,
    Dict,
)

from flask_principal import (
    Identity,
)
from invenio_search.api import RecordsSearchV2

class PaginationParam:
    def apply(
        self,
        identity: Identity,
        search: RecordsSearchV2,
        params: Dict[str, Any],
    ) -> RecordsSearchV2: ...
