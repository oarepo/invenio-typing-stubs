from typing import (
    Any,
    Dict,
    Optional,
    Tuple,
    Type,
    Union,
)

from invenio_records.api import Record
from invenio_records.dumpers.search import SearchDumper
from invenio_records.extensions import ExtensionMixin, RecordExtension, RecordMeta

from oarepo_typing.descriptors import Descriptor

def _get_fields(
    attrs: Any, field_class: Type[SystemField]
) -> Dict[str, SystemField]: ...
def _get_inherited_fields(
    class_: Type[SystemFieldsMixin], field_class: Type[SystemField]
) -> Dict[Any, Any]: ...

class SystemField[R: Record, V: Any](Descriptor[R, V], ExtensionMixin):
    def __init__(self, key: Optional[str] = ...): ...
    @property
    def attr_name(self) -> str: ...
    @property
    def key(self) -> str: ...

class SystemFieldsMixin(metaclass=SystemFieldsMeta):
    """Mixin for classes that support system fields."""

    pass

class SystemFieldContext:
    @property
    def field(self) -> SystemField: ...

class SystemFieldsExt(RecordExtension):
    def __init__(self, declared_fields: Dict[str, SystemField]): ...
    def _run(self, method: str, *args, **kwargs): ...
    def post_commit(self, *args, **kwargs): ...
    def post_create(self, *args, **kwargs): ...
    def post_delete(self, *args, **kwargs): ...
    def post_revert(self, *args, **kwargs): ...
    def pre_commit(self, *args, **kwargs): ...
    def pre_create(self, *args, **kwargs): ...
    def pre_delete(self, *args, **kwargs): ...
    def pre_init(self, *args, **kwargs): ...
    def pre_load(
        self,
        data: Dict[str, Optional[Union[str, int]]],
        loader: Optional[SearchDumper] = ...,
    ): ...
    def pre_revert(self, *args, **kwargs): ...

class SystemFieldsMeta(RecordMeta):
    @staticmethod
    def __new__(
        mcs: Type[SystemFieldsMeta],
        name: str,
        bases: Tuple[()],
        attrs: Dict[str, Union[str, int, Tuple[()]]],
    ) -> SystemFieldsMeta: ...
