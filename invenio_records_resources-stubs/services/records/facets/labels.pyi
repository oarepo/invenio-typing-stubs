from typing import Any

class RecordRelationLabels:
    relation: Any  # Relation field
    lookup_key: str
    def __init__(self, relation: Any, lookup_key: str) -> None: ...
    def __call__(self, ids: list[str]) -> dict[str, Any]: ...
