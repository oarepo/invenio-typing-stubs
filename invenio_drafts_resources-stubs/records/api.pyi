from typing import Generator

from _typeshed import Incomplete
from invenio_drafts_resources.records.systemfields import ParentField as ParentField
from invenio_drafts_resources.records.systemfields import VersionsField as VersionsField
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records_resources.records import Record as RecordBase

class DraftRecordIdProviderV2(RecordIdProviderV2):
    default_status_with_obj: Incomplete

class ParentRecord(RecordBase):
    model_cls: Incomplete
    pid: Incomplete

class Record(RecordBase):
    is_draft: bool
    model_cls: Incomplete
    versions_model_cls: Incomplete
    parent_record_cls: Incomplete
    pid: Incomplete
    is_published: Incomplete
    parent: Incomplete
    versions: Incomplete
    @classmethod
    def get_records_by_parent(
        cls, parent, with_deleted: bool = True, ids_only: bool = False
    ) -> Generator[Record, None, None]: ...
    @classmethod
    def get_latest_by_parent(cls, parent, id_only: bool = False) -> Record | None: ...
    @classmethod
    def publish(cls, draft): ...
    def register(self) -> None: ...

class Draft(Record):
    is_draft: bool
    model_cls: Incomplete
    versions_model_cls: Incomplete
    parent_record_cls: Incomplete
    pid: Incomplete
    parent: Incomplete
    versions: Incomplete
    expires_at: Incomplete
    fork_version_id: Incomplete
    @classmethod
    def new_version(cls, record): ...
    @classmethod
    def edit(cls, record): ...
    @classmethod
    def cleanup_drafts(cls, td, search_gc_deletes: int = 60) -> None: ...
