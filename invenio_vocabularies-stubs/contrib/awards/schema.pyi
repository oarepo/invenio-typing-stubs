from typing import Any

from invenio_vocabularies.contrib.awards.config import award_schemes as award_schemes
from invenio_vocabularies.contrib.funders.schema import (
    FunderRelationSchema as FunderRelationSchema,
)
from invenio_vocabularies.contrib.subjects.schema import (
    SubjectRelationSchema as SubjectRelationSchema,
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
from invenio_vocabularies.services.schema import i18n_strings as i18n_strings
from marshmallow import Schema, validates_schema

class AwardOrganizationRelationSchema(ContribVocabularyRelationSchema):
    ftf_name: str
    parent_field_name: str
    organization: Any
    scheme: Any

class AwardSchema(BaseVocabularySchema, ModePIDFieldVocabularyMixin):
    identifiers: Any
    number: Any
    funder: Any
    acronym: Any
    program: Any
    subjects: Any
    organizations: Any
    start_date: Any
    end_date: Any
    id: Any

class AwardRelationSchema(Schema):
    id: Any
    number: Any
    title = i18n_strings
    identifiers: Any
    acronym: Any
    program: Any
    @validates_schema
    def validate_data(self, data, **kwargs) -> None: ...

class FundingRelationSchema(Schema):
    funder: Any
    award: Any
    @validates_schema
    def validate_data(self, data, **kwargs) -> None: ...
