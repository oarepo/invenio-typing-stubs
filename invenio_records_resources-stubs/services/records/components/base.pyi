from typing import Any, Dict

from flask_principal import (
    Identity,
)
from invenio_search.api import RecordsSearchV2  # type: ignore[import-untyped]

class ServiceComponent:
    def create(self, identity: Identity, **kwargs): ...
    def delete(self, identity: Identity, **kwargs): ...
    def read(self, identity: Identity, **kwargs): ...
    def search(
        self,
        identity: Identity,
        search: RecordsSearchV2,
        params: Dict[str, Any],
        **kwargs,
    ) -> RecordsSearchV2: ...
    def update(self, identity: Identity, **kwargs): ...
