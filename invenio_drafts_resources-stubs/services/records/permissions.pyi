from _typeshed import Incomplete
from invenio_records_permissions.policies.records import RecordPermissionPolicy as RecordPermissionPolicyBase

class RecordPermissionPolicy(RecordPermissionPolicyBase):
    can_create: Incomplete
    can_new_version: Incomplete
    can_edit: Incomplete
    can_publish: Incomplete
    can_read_draft: Incomplete
    can_update_draft: Incomplete
    can_delete_draft: Incomplete
    can_manage_files: Incomplete
