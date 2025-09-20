from _typeshed import Incomplete
from invenio_audit_logs.proxies import (
    current_audit_logs_service as current_audit_logs_service,
)
from invenio_db.uow import Operation
from invenio_records_resources.services.uow import RecordCommitOp

class AuditLogOp(Operation):
    data: Incomplete
    identity: Incomplete
    result: Incomplete
    def __init__(self, data, identity=...) -> None: ...
    def on_register(self, uow) -> None: ...

class AuditRecordCommitOp(RecordCommitOp):
    def on_commit(self, uow): ...
