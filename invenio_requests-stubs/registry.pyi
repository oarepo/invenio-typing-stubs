from typing import (
    Generic,
    Iterator,
    List,
    Optional,
    Type,
    TypeVar,
    overload,
)

_T = TypeVar("_T")

class TypeRegistry(Generic[_T]):
    def __init__(self, types: List[Type[_T]]) -> None: ...
    def __iter__(self) -> Iterator[Type[_T]]: ...
    @overload
    def lookup(self, type_id: str, quiet: bool = ...) -> Type[_T]: ...
    @overload
    def lookup(
        self, type_id: str, quiet: bool, default: Optional[Type[_T]]
    ) -> Optional[Type[_T]]: ...
    def register_type(self, type_: Type[_T], force: bool = ...) -> None: ...
