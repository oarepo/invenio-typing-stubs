from invenio_records_resources.services.records.results import RecordList
from invenio_vocabularies.proxies import current_service as current_service

class VocabularyTypeList(RecordList):
    @property
    def custom_vocabulary_names(self) -> list[str]: ...
