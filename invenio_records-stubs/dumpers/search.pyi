from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Type,
    Union,
)
from uuid import UUID

from invenio_records.api import Record
from invenio_records.dumpers.indexedat import IndexedAtDumperExt
from invenio_records.dumpers.relations import RelationDumperExt

class SearchDumper[R: Record = Record]:
    def __init__(
        self,
        extensions: Optional[
            Union[List[RelationDumperExt], List[IndexedAtDumperExt]]
        ] = ...,
        model_fields: None = ...,
    ): ...
    @staticmethod
    def _deserialize(
        value: Union[str, int], dump_type: Union[Type[int], Type[UUID], Type[datetime]]
    ) -> Union[datetime, UUID, int]: ...
    def _dump_model_field(
        self,
        record: R,
        model_field_name: str,
        dump: Dict[str, Any],
        dump_key: str,
        dump_type: Union[Type[int], Type[UUID], Type[datetime]],
    ): ...
    @staticmethod
    def _iter_modelfields(record_cls: Type[R]): ...
    def _load_model_field(
        self,
        record_cls: Type[R],
        model_field_name: str,
        dump: Dict[str, Any],
        dump_key: str,
        dump_type: Union[Type[int], Type[UUID], Type[datetime]],
    ) -> Optional[Union[datetime, UUID, int]]: ...
    @staticmethod
    def _serialize(
        value: Optional[Union[datetime, UUID, int]],
        dump_type: Union[Type[int], Type[UUID], Type[datetime]],
    ) -> Optional[Union[str, int]]: ...
    def dump(self, record: R, data: Dict[Any, Any]) -> Dict[str, Any]: ...
    def load(self, dump_data: Dict[str, Any], record_cls: Type[R]) -> R: ...

class SearchDumperExt:
    def dump(self, record: Record, data: Dict[Any, Any]) -> Any: ...
    def load(self, data: Dict[str, Any], record_cls: Type[Record]) -> Any: ...
