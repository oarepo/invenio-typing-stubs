from typing import (
    Dict,
    Optional,
    Tuple,
    Type,
    Union,
)

from invenio_records.dumpers.search import SearchDumper

class ExtensionMixin:
    def pre_load(
        self,
        data: Dict[str, Optional[Union[str, int]]],
        loader: Optional[SearchDumper] = ...,
    ): ...

class RecordMeta:
    @staticmethod
    def __new__(
        mcs: Type[RecordMeta],
        name: str,
        bases: Tuple[()],
        attrs: Dict[str, Union[str, int, Tuple[()]]],
    ) -> RecordMeta: ...
