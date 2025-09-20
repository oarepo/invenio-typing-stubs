from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)

from invenio_records.api import Record

def clear_none(d: Any): ...
def clear_none_list(
    ls: List[Optional[Union[Dict[str, Optional[str]], Dict[str, None], str, Any]]],
): ...
def dict_lookup(
    source: Union[
        Dict[str, Union[str, Dict[str, str]]],
        Dict[str, str],
        Dict[str, Union[int, Dict[str, None], List[str]]],
        Record,
    ],
    lookup_key: str,
    parent: bool = ...,
) -> Optional[Union[int, Dict[str, None], str, List[str]]]: ...
def dict_merge(
    dest: Dict[str, Union[str, Dict[str, int], int]],
    source: Dict[str, Union[str, Dict[str, str]]],
): ...
def dict_set(
    source: Dict[str, Any],
    key: str,
    value: Union[
        Dict[str, str],
        str,
        Dict[str, Union[str, Dict[str, str]]],
        List[Dict[str, Union[str, Dict[str, str]]]],
    ],
): ...
def filter_dict_keys(
    src: Dict[str, Union[int, Dict[str, int], Dict[str, Union[Dict[str, int], int]]]],
    keys: List[str],
) -> Dict[str, Union[int, Dict[str, int], Dict[str, Union[Dict[str, int], int]]]]: ...
def parse_lookup_key(lookup_key: Union[str, List[str]]) -> List[str]: ...
