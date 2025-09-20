# Invenio-Records package typing stubs
from invenio_records.api import Record as Record
from invenio_records.api import RecordBase as RecordBase
from invenio_records.api import RecordRevision as RecordRevision
from invenio_records.api import RevisionsIterator as RevisionsIterator
from invenio_records.ext import InvenioRecords as InvenioRecords
from invenio_records.models import RecordMetadata as RecordMetadata
from invenio_records.models import RecordMetadataBase as RecordMetadataBase

__version__: str

__all__: list[str] = [
    "InvenioRecords",
    "Record",
    "RecordBase",
    "RecordMetadata",
    "RecordMetadataBase",
    "RecordRevision",
    "RevisionsIterator",
    "__version__",
]
