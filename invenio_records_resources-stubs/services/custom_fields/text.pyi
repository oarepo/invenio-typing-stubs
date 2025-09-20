from typing import Any, Dict, Type, Union

from marshmallow_utils.fields.sanitizedhtml import SanitizedHTML
from marshmallow_utils.fields.sanitizedunicode import SanitizedUnicode

class KeywordCF:
    def __init__(
        self,
        name: str,
        field_cls: Union[Type[SanitizedUnicode], Type[SanitizedHTML]] = ...,
        **kwargs,
    ): ...
    @property
    def mapping(self) -> Dict[str, str]: ...

class TextCF:
    def __init__(
        self,
        name: str,
        field_cls: Union[Type[SanitizedUnicode], Type[SanitizedHTML]] = ...,
        use_as_filter: bool = ...,
        **kwargs,
    ): ...
    @property
    def mapping(self) -> Dict[str, Any]: ...
