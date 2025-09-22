from typing import Any, Dict

class CustomFieldsSchema:
    field_property_name: str
    def __init__(self, fields_var: str, *args, **kwargs): ...
    def _serialize(self, obj: Any, **kwargs) -> Dict[str, Any]: ...
    def _deserialize(self, data: Dict[str, Any], **kwargs) -> Dict[str, Any]: ...

class CustomFieldsSchemaUI(CustomFieldsSchema):
    field_property_name: str
