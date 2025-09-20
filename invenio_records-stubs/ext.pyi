from typing import (
    Any,
    Dict,
    Optional,
    Union,
)

from flask.app import Flask
from invenio_records.api import Record
from jsonref import JsonRef  # type: ignore[import-untyped]

class InvenioRecords:
    def __init__(self, app: Optional[Flask] = ..., **kwargs): ...
    def init_app(
        self, app: Flask, entry_point_group: str = ..., **kwargs
    ) -> _RecordsState: ...
    def init_config(self, app: Flask): ...

class _RecordsState:
    def __init__(self, app: Flask, entry_point_group: Optional[str] = ...): ...
    def replace_refs(self, data: Record) -> Dict[str, Union[JsonRef, int]]: ...
    def validate(self, data: Dict[str, Any], schema: Any, **kwargs) -> None: ...
