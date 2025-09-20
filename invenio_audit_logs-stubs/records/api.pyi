from _typeshed import Incomplete
from invenio_audit_logs.records import models
from invenio_records.dumpers import SearchDumper
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField

class AuditLog(Record):
    model_cls = models.AuditLog
    dumper: SearchDumper
    index: IndexField
    id: Incomplete
    created: Incomplete
    action: Incomplete
    user_id: Incomplete
    user: Incomplete
    resource_type: Incomplete
    resource: Incomplete
