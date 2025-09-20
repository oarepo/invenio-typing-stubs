from typing import (
    Optional,
    Type,
)

import marshmallow as ma
from invenio_records_resources.records.systemfields.pid import PIDField

class RecordTypeFactory:
    def __init__(
        self,
        record_type_name: str,
        service_schema: Type[ma.Schema],
        schema_version: str = ...,
        endpoint_route: Optional[str] = ...,
        record_dumper: None = ...,
        record_relations: None = ...,
        schema_path: Optional[str] = ...,
        index_name: Optional[str] = ...,
        search_options: None = ...,
        service_components: None = ...,
        permission_policy_cls: None = ...,
        pid_field_cls: Type[PIDField] = ...,
        pid_field_kwargs: None = ...,
        model_cls_attrs: None = ...,
        record_cls_attrs: None = ...,
        resource_cls_attrs: None = ...,
        service_id: None = ...,
    ): ...
    def _build_index_name(self, index_name: Optional[str]) -> str: ...
    def _build_schema_path(self, optional_schema_path: Optional[str]) -> str: ...
    def create_metadata_model(self): ...
    def create_record_class(self): ...
    def create_record_type(self): ...
    def create_resource_class(self): ...
    def create_service_class(self): ...
    def validate(self): ...
