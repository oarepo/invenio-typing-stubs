from typing import Any

from invenio_audit_logs.services import AuditLogAction
from invenio_drafts_resources.auditlog.context import RecordContext as RecordContext
from invenio_drafts_resources.auditlog.context import RequestContext as RequestContext
from invenio_drafts_resources.auditlog.context import UserContext as UserContext

class RecordBaseAuditLog(AuditLogAction):
    context: list[Any]
    resource_type: str

class DraftCreateAuditLog(RecordBaseAuditLog):
    context: list[Any]
    message_template: str

class DraftEditAuditLog(RecordBaseAuditLog):
    context: list[Any]
    message_template: str

class RecordPublishAuditLog(RecordBaseAuditLog):
    context: list[Any]
    id: str
    message_template: str

class DraftDeleteAuditLog(RecordBaseAuditLog):
    id: str
    message_template: str

class DraftNewVersionAuditLog(RecordBaseAuditLog):
    id: str
    message_template: str
