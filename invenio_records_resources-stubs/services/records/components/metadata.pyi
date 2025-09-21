from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from flask_principal import (
    Identity,
)
from invenio_records_resources.records.api import (
    Record,
)
from invenio_records_resources.services.records.components.base import ServiceComponent

class MetadataComponent(ServiceComponent):
    def create(
        self,
        identity: Identity,
        data: Optional[Dict[str, Any]] = ...,
        record: Optional[Record] = ...,
        errors: Optional[List[Any]] = ...,
        **kwargs,
    ): ...
    def update(
        self,
        identity: Identity,
        data: Optional[Dict[str, Any]] = ...,
        record: Record = ...,
        **kwargs,
    ): ...
