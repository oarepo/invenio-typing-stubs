from invenio_records.dumpers import SearchDumper
from invenio_records.systemfields import ConstantField, RelatedModelField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField, PIDField
from invenio_vocabularies.records.models import VocabularyMetadata as VocabularyMetadata
from invenio_vocabularies.records.models import VocabularyType as VocabularyType
from invenio_vocabularies.records.pidprovider import (
    VocabularyIdProvider as VocabularyIdProvider,
)
from invenio_vocabularies.records.systemfields import (
    VocabularyPIDFieldContext as VocabularyPIDFieldContext,
)

class Vocabulary(Record):
    schema: ConstantField
    index: IndexField
    metadata: None
    type: RelatedModelField
    pid: PIDField
    dumper: SearchDumper
