from _typeshed import Incomplete
from invenio_records.models import RecordMetadataBase
from sqlalchemy.ext.declarative import declared_attr

class ParentRecordMixin:
    __parent_record_model__: Incomplete
    @declared_attr
    def parent_id(cls): ...
    @declared_attr
    def parent(cls): ...
    index: Incomplete

class ParentRecordStateMixin:
    __parent_record_model__: Incomplete
    __record_model__: Incomplete
    __draft_model__: Incomplete
    @declared_attr
    def parent_id(cls): ...
    @declared_attr
    def latest_id(cls): ...
    latest_index: Incomplete
    @declared_attr
    def next_draft_id(cls): ...

class DraftMetadataBase(RecordMetadataBase):
    fork_version_id: Incomplete
    expires_at: Incomplete
