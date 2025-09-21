from typing import (
    Any,
    Dict,
)

from flask_principal import (
    Identity,
)
from invenio_search.api import RecordsSearchV2  # type: ignore[import-untyped]

class QueryStrParam:
    def apply(
        self,
        identity: Identity,
        search: RecordsSearchV2,
        params: Dict[str, Any],
    ) -> RecordsSearchV2: ...
