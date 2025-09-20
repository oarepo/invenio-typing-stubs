from typing import TYPE_CHECKING, Optional

from invenio_db import db
from invenio_records.models import RecordMetadataBase
from sqlalchemy import Column

if TYPE_CHECKING:
    from invenio_records.systemfields.relatedmodelfield import RelatedModelField
    from invenio_vocabularies.records.api import Vocabulary

class VocabularyType(db.Model):
    __tablename__: str
    id: Column[str]
    pid_type: Column[str]
    @classmethod
    def create(cls, **data) -> VocabularyType: ...
    @classmethod
    def dump_obj(
        cls, field: RelatedModelField, record: Vocabulary, obj: VocabularyType
    ) -> None: ...
    @classmethod
    def load_obj(
        cls, field: RelatedModelField, record: Vocabulary
    ) -> Optional[VocabularyType]: ...

class VocabularyMetadata(db.Model, RecordMetadataBase):
    __tablename__: str

class VocabularyScheme(db.Model):
    __tablename__: str
    id: Column[str]
    parent_id: Column[str]
    name: Column[str]
    uri: Column[str]
    @classmethod
    def create(cls, **data) -> VocabularyScheme: ...
