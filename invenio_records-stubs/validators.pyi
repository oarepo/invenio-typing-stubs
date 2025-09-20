from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

from jsonschema.validators import Draft202012Validator  # type: ignore[import-untyped]

def _create_validator(
    schema: Dict[
        str,
        Union[
            Dict[str, Dict[str, str]],
            List[str],
            str,
            Dict[str, Dict[str, Union[str, int]]],
            Dict[
                str,
                Union[Dict[str, str], Dict[str, Union[str, Dict[str, Dict[str, str]]]]],
            ],
        ],
    ],
    base_validator_cls: None = ...,
    custom_checks: Optional[Dict[Any, Any]] = ...,
) -> Type[Draft202012Validator]: ...
def _generate_legacy_type_checks(
    types: Dict[str, Tuple[Type[list], Type[tuple]]],
) -> Dict[str, Callable]: ...
