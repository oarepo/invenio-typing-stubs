from marshmallow.exceptions import ValidationError
from typing import (
    Any,
    Dict,
    List,
    Union,
)


def _iter_errors_dict(message_node: Any, fieldpath: str = ...): ...


def validation_error_to_list_errors(
    exception: ValidationError
) -> List[Dict[str, Union[str, List[str]]]]: ...
