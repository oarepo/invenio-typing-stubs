from typing import Type

from invenio_records_resources.services.records.config import RecordServiceConfig
from invenio_vocabularies.contrib.subjects.subjects import record_type as record_type
from invenio_vocabularies.records.models import VocabularyScheme as VocabularyScheme

SubjectsServiceConfig: Type[RecordServiceConfig]

class SubjectsService(record_type.service_cls):
    def create_scheme(self, identity, id_, name: str = "", uri: str = ""): ...
