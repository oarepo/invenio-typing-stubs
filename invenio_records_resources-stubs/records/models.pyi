from typing import ClassVar

from _typeshed import Incomplete
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql.schema import Column

class FileRecordModelMixin:
    __record_model_cls__: ClassVar[type[Incomplete] | None]
    key: Column
    @declared_attr
    def record_id(cls) -> Column: ...  # Column
    @declared_attr
    def record(cls) -> Incomplete: ...  # relationship
    @declared_attr
    def object_version_id(cls) -> Column: ...  # Column
    @declared_attr
    def object_version(cls) -> Incomplete: ...  # relationship
    @declared_attr
    def __table_args__(cls) -> Incomplete: ...
