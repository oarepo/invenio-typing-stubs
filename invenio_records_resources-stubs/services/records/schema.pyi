from typing import (
    Any,
    Dict,
    List,
    Optional,
    Tuple,
)

import marshmallow as ma
from invenio_records_resources.records.api import (
    Record,
)
from invenio_records_resources.services.base import Service

class BaseRecordSchema(ma.Schema):
    def clean(self, input_data: Dict[str, Any], **kwargs) -> Dict[str, Any]: ...

class ServiceSchemaWrapper:
    def __init__(
        self,
        service: Service,
        schema: ma.Schema,
    ): ...
    def _build_context(self, base_context: Dict[str, Any]) -> Dict[str, Any]: ...
    def dump(
        self,
        data: Record,
        schema_args: None = ...,
        context: Optional[Dict[str, Any]] = ...,
    ) -> Dict[str, Any]: ...
    def load(
        self,
        data: Dict[str, Any],
        schema_args: None = ...,
        context: Optional[Dict[str, Any]] = ...,
        raise_errors: bool = ...,
    ) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]: ...
