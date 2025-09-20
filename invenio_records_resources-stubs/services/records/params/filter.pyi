from typing import Any

from invenio_records_resources.services.records.params import (
    ParamInterpreter as ParamInterpreter,
)

class FilterParam(ParamInterpreter):
    param_name: str
    field_name: str
    def __init__(self, param_name: str, field_name: str, config: Any) -> None: ...
    @classmethod
    def factory(
        cls, param: str | None = None, field: str | None = None
    ) -> type["FilterParam"]: ...
    def apply(self, identity: Any, search: Any, params: dict[str, Any]) -> Any: ...
