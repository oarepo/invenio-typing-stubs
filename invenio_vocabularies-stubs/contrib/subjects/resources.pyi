from typing import Type

from invenio_records_resources.resources import RecordResource, RecordResourceConfig
from invenio_vocabularies.contrib.subjects.subjects import record_type as record_type

SubjectsResourceConfig: Type[RecordResourceConfig]
SubjectsResource: Type[RecordResource]
