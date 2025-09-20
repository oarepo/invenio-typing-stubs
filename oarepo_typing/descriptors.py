from typing import Generic, Self, TypeVar, overload

T = TypeVar("T")  # owner type
V = TypeVar("V")  # value type


# only for type checking inside the .pyi file, not in runtime
class Descriptor(Generic[T, V]):
    @overload
    def __get__(self, instance: None, owner: type[T]) -> Self: ...
    @overload
    def __get__(self, instance: T, owner: type[T]) -> V: ...
    def __get__(self, instance: T | None, owner: type[T]) -> V | Self: ...  # type: ignore
    def __set__(self, instance: T, value: V) -> None: ...
