from typing import Any, Optional, Type

import marshmallow as ma
from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_resources.records.systemfields.pid import PIDField
from invenio_records_resources.services.records.config import SearchOptions

class RecordTypeFactory:
    # Class attributes populated during creation
    model_cls: Optional[Type[Any]]
    record_cls: Optional[Type[Any]]
    resource_cls: Optional[Type[Any]]
    resource_config_cls: Optional[Type[Any]]
    service_config_cls: Optional[Type[Any]]
    service_cls: Optional[Type[Any]]

    _schema_path_template: str
    _index_name_template: str

    # Instance attributes set in constructor
    record_type_name: str
    record_name_lower: str
    name_plural: str
    pid_field_cls: Type[PIDField]
    pid_field_kwargs: dict[str, Any]
    schema_version: str
    record_dumper: Optional[Any]
    record_relations: Optional[Any]
    schema_path: str
    index_name: str
    model_cls_attrs: dict[str, Any]
    record_cls_attrs: dict[str, Any]
    resource_cls_attrs: dict[str, Any]
    endpoint_route: Optional[str]
    service_id: Optional[str]
    service_schema: Type[ma.Schema]
    search_options: Type[SearchOptions]
    service_components: Optional[list[Type[Any]]]
    permission_policy_cls: Optional[Type[RecordPermissionPolicy]]

    # Constructor
    def __init__(
        self,
        record_type_name: str,
        service_schema: Type[ma.Schema],
        schema_version: str = ...,
        endpoint_route: Optional[str] = ...,
        record_dumper: Optional[Any] = ...,
        record_relations: Optional[Any] = ...,
        schema_path: Optional[str] = ...,
        index_name: Optional[str] = ...,
        search_options: Type[SearchOptions] | SearchOptions | None = ...,
        service_components: Optional[list[Type[Any]]] = ...,
        permission_policy_cls: Optional[Type[RecordPermissionPolicy]] = ...,
        pid_field_cls: Type[PIDField] = ...,
        pid_field_kwargs: Optional[dict[str, Any]] = ...,
        model_cls_attrs: Optional[dict[str, Any]] = ...,
        record_cls_attrs: Optional[dict[str, Any]] = ...,
        resource_cls_attrs: Optional[dict[str, Any]] = ...,
        service_id: Optional[str] = ...,
    ) -> None: ...

    # Helpers
    def _build_index_name(self, index_name: Optional[str]) -> str: ...
    def _build_schema_path(self, optional_schema_path: Optional[str]) -> str: ...

    # Factory steps
    def create_metadata_model(self) -> None: ...
    def create_record_class(self) -> None: ...
    def create_resource_class(self) -> None: ...
    def create_service_class(self) -> None: ...
    def create_record_type(self) -> None: ...
    def validate(self) -> None: ...
