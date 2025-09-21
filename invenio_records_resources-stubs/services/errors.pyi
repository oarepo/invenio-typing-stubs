from typing import Any, Dict, List, Optional, Union

from flask_principal import PermissionDenied
from marshmallow import ValidationError

class RecordPermissionDeniedError(PermissionDenied):
    """Record permission denied error."""

    description: str
    record: Any
    action_name: Optional[str]

    def __init__(
        self,
        action_name: Optional[str] = ...,
        record: Any = ...,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...

class PermissionDeniedError(PermissionDenied):
    """Permission denied error."""

    @property
    def description(self) -> str: ...

class RevisionIdMismatchError(Exception):
    """Etag check exception."""

    record_revision_id: int
    expected_revision_id: int

    def __init__(self, record_revision_id: int, expected_revision_id: int) -> None: ...
    @property
    def description(self) -> str: ...

class QuerystringValidationError(ValidationError):
    """Error thrown when there is an issue with the querystring."""

    ...

class ValidationErrorGroup(Exception):
    """Error containing multiple validation errors."""

    errors: List[Dict[str, Union[str, List[str]]]]

    def __init__(self, errors: List[Dict[str, Union[str, List[str]]]]) -> None: ...

class TransferException(Exception):
    """File transfer exception."""

    ...

class FacetNotFoundError(Exception):
    """Facet not found exception."""

    vocabulary_id: Any

    def __init__(self, vocabulary_id: Any) -> None: ...

class FileKeyNotFoundError(Exception):
    """Error denoting that a record doesn't have a certain file."""

    recid: str
    file_key: str

    def __init__(self, recid: str, file_key: str) -> None: ...

class FailedFileUploadException(Exception):
    """File failed to upload exception."""

    recid: str
    file_key: str
    file: Any

    def __init__(self, recid: str, file: Any, file_key: str) -> None: ...

class FilesCountExceededException(Exception):
    """Files count is exceeding the max allowed exception."""

    def __init__(self, max_files: int, resulting_files_count: int) -> None: ...
