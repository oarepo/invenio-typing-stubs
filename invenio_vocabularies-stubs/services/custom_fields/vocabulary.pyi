from typing import Any, Dict, List, Optional

import marshmallow as ma
from flask_principal import Identity
from invenio_records_resources.services.custom_fields.base import BaseCF
from invenio_vocabularies.proxies import current_service as current_service
from invenio_vocabularies.records.api import Vocabulary as Vocabulary
from invenio_vocabularies.resources.serializer import (
    VocabularyL10NItemSchema as VocabularyL10NItemSchema,
)
from invenio_vocabularies.services.schema import (
    VocabularyRelationSchema as VocabularyRelationSchema,
)
from marshmallow.fields import Field

class VocabularyCF(BaseCF):
    field_keys: List[str]
    relation_cls: type
    vocabulary_id: str
    dump_options: bool
    multiple: bool
    sort_by: Optional[str]
    schema: type[ma.Schema]
    ui_schema: type[ma.Schema]
    pid_field: Any
    def __init__(
        self,
        name: str,
        vocabulary_id: str,
        multiple: bool = False,
        dump_options: bool = True,
        sort_by=None,
        schema: type[ma.Schema] = ...,
        ui_schema: type[ma.Schema] = ...,
        **kwargs: Any,
    ) -> None: ...
    def options(self, identity: Identity) -> Optional[List[Dict[str, Any]]]: ...
    @property
    def field(self) -> Field: ...
    @property
    def mapping(self) -> Any: ...
