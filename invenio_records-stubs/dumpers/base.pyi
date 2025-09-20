from typing import (
    Any,
    Dict,
    List,
    Union,
)

from invenio_records.api import Record

class Dumper[R: Record = Record]:
    def dump(self, record: R, data: Dict[Any, Any]) -> Dict[
        str,
        Union[
            Dict[str, str],
            str,
            Dict[str, Union[str, Dict[str, Dict[str, str]], List[str]]],
            Dict[str, Dict[str, str]],
            List[str],
        ],
    ]: ...
