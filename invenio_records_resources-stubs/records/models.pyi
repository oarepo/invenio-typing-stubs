from typing import Any

from sqlalchemy.ext.declarative import declared_attr

class FileRecordModelMixin:
    __record_model_cls__: type[Any] | None
    key: Any  # Column
    @declared_attr
    def record_id(cls) -> Any: ...  # Column
    @declared_attr
    def record(cls) -> Any: ...  # relationship
    @declared_attr
    def object_version_id(cls) -> Any: ...  # Column
    @declared_attr
    def object_version(cls) -> Any: ...  # relationship
    @declared_attr
    def __table_args__(cls) -> Any: ...
