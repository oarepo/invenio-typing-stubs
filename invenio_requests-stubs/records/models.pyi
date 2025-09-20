from datetime import datetime
from typing import Optional
from uuid import UUID

from invenio_db import db
from invenio_records.models import RecordMetadataBase
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped

class RequestMetadata(db.Model, RecordMetadataBase):
    __tablename__: str
    id: Mapped[UUID]
    number: Optional[str]
    expires_at: Optional[datetime]

class RequestEventModel(db.Model, RecordMetadataBase):
    __tablename__: str
    type: str
    request_id: UUID
    request: RequestMetadata

class SequenceMixin:
    @declared_attr
    def value(cls) -> Column[int]: ...
    @classmethod
    def _set_sequence(cls, val: int) -> None: ...
    @classmethod
    def insert(cls, val: int) -> None: ...
    @classmethod
    def max(cls) -> int: ...
    @classmethod
    def next(cls) -> int: ...

class RequestNumber(db.Model, SequenceMixin):
    __tablename__: str
