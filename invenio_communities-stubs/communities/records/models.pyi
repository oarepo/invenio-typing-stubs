from typing import Any, Optional

from invenio_communities.communities.records.systemfields.deletion_status import (
    CommunityDeletionStatusEnum as CommunityDeletionStatusEnum,
)
from invenio_db import db
from invenio_records.models import RecordMetadataBase, Timestamp
from invenio_records_resources.records import FileRecordModelMixin

class CommunityMetadata(db.Model, RecordMetadataBase):
    __tablename__: str
    slug: str
    bucket_id: Any
    bucket: Any
    deletion_status: CommunityDeletionStatusEnum

class CommunityFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    __record_model_cls__ = CommunityMetadata
    __tablename__: str

class CommunityFeatured(db.Model, Timestamp):
    __tablename__: str
    id: Any
    community_id: Any
    start_date: Optional[Any]
