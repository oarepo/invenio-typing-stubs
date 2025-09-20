from typing import Any, Callable, Optional, Type

from invenio_records.api import Record
from invenio_records.systemfields.base import SystemField, SystemFieldContext

class RelatedModelFieldContext[R: Record = Record](SystemFieldContext):
    def session_merge(self, record: R) -> None: ...

class RelatedModelField[R: Record = Record, M: Any = Any](SystemField[R, Optional[M]]):
    _model: Type[M]
    _required: bool
    _load: Callable[..., Optional[M]]
    _dump: Callable[..., None]
    _context_cls: Type[RelatedModelFieldContext[R]]

    def __init__(
        self,
        model: Type[M],
        key: Optional[str] = ...,
        required: bool = ...,
        load: Optional[Callable[..., Optional[M]]] = ...,
        dump: Optional[Callable[..., None]] = ...,
        context_cls: Optional[Type[RelatedModelFieldContext[R]]] = ...,
    ): ...
    def pre_commit(self, record: R) -> None: ...
    def obj(self, record: R) -> Optional[M]: ...
    def set_obj(self, record: R, obj: M) -> None: ...
