from typing import Sequence, Type

from invenio_records_permissions.generators import Generator
from invenio_records_permissions.policies.base import BasePermissionPolicy

def obj_or_import_string(value, default=None): ...

class RecordPermissionPolicy(BasePermissionPolicy):
    NEED_LABEL_TO_ACTION: dict[str, str]
    can_read_files: Sequence[Generator]
    can_update_files: Sequence[Generator]
    can_read_deleted_files: Sequence[Generator]
    can_create_or_update_many: Sequence[Generator]
    original_action: str
    def __init__(self, action: str, **over) -> None: ...

def get_record_permission_policy() -> Type[RecordPermissionPolicy]: ...
