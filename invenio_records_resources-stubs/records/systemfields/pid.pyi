from typing import (
    Any,
    Optional,
    Type,
)

from invenio_pidstore.models import PersistentIdentifier
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import RelatedModelFieldContext
from invenio_records.systemfields.base import SystemField
from invenio_records_resources.records.api import (
    Record,
)
from invenio_records_resources.records.providers import ModelPIDProvider
from invenio_records_resources.records.resolver import ModelResolver

class PIDFieldContext[R: Record = Record](RelatedModelFieldContext[R]):
    def resolve(
        self,
        pid_value: str,
        registered_only: bool = ...,
        with_deleted: bool = ...,
    ) -> R: ...

class PIDField[R: Record = Record](SystemField[R, PIDFieldContext[R]]):
    def __init__(
        self,
        key: str = ...,
        provider: Optional[Type[RecordIdProviderV2]] = ...,
        pid_type: str = ...,
        object_type: str = ...,
        resolver_cls: None = ...,
        delete: bool = ...,
        create: bool = ...,
        context_cls: Type[PIDFieldContext] = ...,
    ): ...
    def create(self, record: R) -> PersistentIdentifier: ...
    def delete(self, record: R): ...
    @staticmethod
    def dump_obj(field: Any, record: Any, pid: PersistentIdentifier): ...
    @staticmethod
    def load_obj(field: Any, record: Any) -> PersistentIdentifier: ...
    def post_create(self, record: R): ...
    def post_delete(self, record: R, force: bool = ...): ...

class ModelPIDFieldContext[R: Record = Record](PIDFieldContext[R]):
    def resolve(
        self, pid_value: str, registered_only: bool = True, with_deleted: bool = False
    ): ...
    def create(self, record: R) -> PersistentIdentifier: ...
    def session_merge(self, record: R) -> None: ...

class ModelPIDField[R: Record = Record](SystemField[R, ModelPIDFieldContext[R]]):
    def __init__(
        self,
        model_field_name: str = ...,
        provider: Type[ModelPIDProvider] = ...,
        resolver_cls: Type[ModelResolver] = ...,
        context_cls: Type[ModelPIDFieldContext] = ...,
    ): ...
