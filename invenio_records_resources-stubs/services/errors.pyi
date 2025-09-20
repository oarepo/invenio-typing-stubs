from typing import (
    Dict,
    List,
    Union,
)


class FileKeyNotFoundError:
    def __init__(self, recid: str, file_key: str): ...


class RevisionIdMismatchError:
    def __init__(self, record_revision_id: int, expected_revision_id: int): ...
    @property
    def description(self) -> str: ...


class ValidationErrorGroup:
    def __init__(self, errors: List[Dict[str, Union[str, List[str]]]]): ...
