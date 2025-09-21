from typing import (
    Dict,
    Optional,
    Tuple,
    Type,
    Union,
)

from invenio_records.dumpers import Dumper

class ExtensionMixin:
    def pre_load(
        self,
        data: Dict[str, Optional[Union[str, int]]],
        loader: Optional[Dumper] = ...,
    ): ...

class RecordExtension(ExtensionMixin): ...

class RecordMeta(type):
    @staticmethod
    def __new__(
        mcs: Type[RecordMeta],
        name: str,
        bases: Tuple[()],
        attrs: Dict[str, Union[str, int, Tuple[()]]],
    ) -> RecordMeta: ...
