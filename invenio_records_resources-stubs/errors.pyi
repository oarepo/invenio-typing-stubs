from typing import (
    Any,
    Dict,
    Generator,
    List,
    Union,
)

from marshmallow.exceptions import ValidationError

def _iter_errors_dict(
    message_node: Union[Dict[str, Any], List[str], str], fieldpath: str = ...
) -> Generator[Dict[str, Union[str, List[str]]], None, None]: ...
def validation_error_to_list_errors(
    exception: ValidationError,
) -> List[Dict[str, Union[str, List[str]]]]: ...
