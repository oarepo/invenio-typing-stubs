from marshmallow import Schema, validates_schema

class EntityReferenceBaseSchema(Schema):
    @validates_schema
    def there_can_be_only_one(self, data, **kwargs) -> None: ...
    @classmethod
    def create_from_dict(cls, allowed_types, special_fields=None): ...

class MultipleEntityReferenceBaseSchema(EntityReferenceBaseSchema):
    @classmethod
    def create_from_dict(cls, allowed_types, special_fields=None): ...
