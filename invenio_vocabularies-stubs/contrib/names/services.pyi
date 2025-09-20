from typing import Type

from invenio_records_resources.services.records.config import RecordServiceConfig
from invenio_vocabularies.contrib.names.names import record_type as record_type

NamesServiceConfig: Type[RecordServiceConfig]

class NamesService(record_type.service_cls):
    def resolve(self, identity, id_, id_type, many: bool = False): ...
