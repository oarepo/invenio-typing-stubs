from typing import Any, Dict, Type, Union

from invenio_records_resources.services.custom_fields.base import BaseListCF
from marshmallow_utils.fields.sanitizedhtml import SanitizedHTML
from marshmallow_utils.fields.sanitizedunicode import SanitizedUnicode

class KeywordCF(BaseListCF):
    def __init__(
        self,
        name: str,
        field_cls: Union[Type[SanitizedUnicode], Type[SanitizedHTML]] = ...,
        **kwargs,
    ): ...
    @property
    def mapping(self) -> Dict[str, str]: ...

class TextCF(KeywordCF):
    def __init__(
        self,
        name: str,
        field_cls: Union[Type[SanitizedUnicode], Type[SanitizedHTML]] = ...,
        use_as_filter: bool = ...,
        **kwargs,
    ): ...
    @property
    def mapping(self) -> Dict[str, Any]: ...
