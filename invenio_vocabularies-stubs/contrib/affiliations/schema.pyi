from typing import Any

from invenio_vocabularies.contrib.affiliations.config import (
    affiliation_schemes as affiliation_schemes,
)
from invenio_vocabularies.services.schema import (
    BaseVocabularySchema as BaseVocabularySchema,
)
from invenio_vocabularies.services.schema import (
    ContribVocabularyRelationSchema as ContribVocabularyRelationSchema,
)
from invenio_vocabularies.services.schema import (
    ModePIDFieldVocabularyMixin as ModePIDFieldVocabularyMixin,
)

class AffiliationSchema(BaseVocabularySchema, ModePIDFieldVocabularyMixin):
    acronym: Any
    identifiers: Any
    name: Any
    country: Any
    country_name: Any
    location_name: Any
    id: Any
    aliases: Any
    status: Any
    types: Any

class AffiliationRelationSchema(ContribVocabularyRelationSchema):
    ftf_name: str
    parent_field_name: str
    name: Any
    identifiers: Any
