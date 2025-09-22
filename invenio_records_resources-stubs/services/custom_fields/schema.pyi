from typing import Any, Dict, Iterable, Mapping

from marshmallow import Schema

class CustomFieldsSchema(Schema):
    field_property_name: str
    def __init__(self, fields_var: str, *args, **kwargs): ...
    def _serialize(self, obj: Any, **kwargs) -> Dict[str, Any]: ...
    def _deserialize(
        self, data: Mapping[str, Any] | Iterable[Mapping[str, Any]], **kwargs
    ) -> Dict[str, Any]: ...

class CustomFieldsSchemaUI(CustomFieldsSchema):
    field_property_name: str
