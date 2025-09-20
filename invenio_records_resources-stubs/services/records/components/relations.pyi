from typing import Any, Dict, Optional

from flask_principal import Identity
from invenio_records_resources.records.api import (
    Record,
)

class ChangeNotificationsComponent:
    def update(
        self,
        identity: Identity,
        data: Optional[Dict[str, Any]] = ...,
        record: Optional[Record] = ...,
        uow: None = ...,
        **kwargs,
    ): ...

class RelationsComponent:
    def read(self, identity: Identity, record: Optional[Record] = ...): ...
