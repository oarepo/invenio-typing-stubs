from _typeshed import Incomplete
from invenio_db import db
from invenio_records.models import RecordMetadataBase

class AuditLog(db.Model, RecordMetadataBase):
    __tablename__: str
    encoder: Incomplete
    action: Incomplete
    resource_type: Incomplete
    user_id: Incomplete
