from invenio_records_resources.services.custom_fields.text import TextCF
from typing import (
    List,
    Optional,
    Set,
)


def validate_custom_fields(
    available_fields: List[TextCF],
    namespaces: Optional[Set[str]] = ...,
    given_fields: Optional[List[str]] = ...
): ...
