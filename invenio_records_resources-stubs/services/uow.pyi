from typing import (
    Any,
    List,
    Optional,
    Union,
)

from invenio_db.uow import Operation, UnitOfWork  # noqa
from invenio_indexer.api import RecordIndexer
from invenio_records_resources.records.api import FileRecord, Record

class ChangeNotificationOp:
    def __init__(self, record_type: str, records: List[Record]): ...
    def on_post_commit(self, uow: UnitOfWork): ...

class RecordBulkCommitOp:
    def __init__(
        self,
        records: List[Record],
        indexer: Optional[RecordIndexer] = ...,
        index_refresh: bool = ...,
    ): ...
    def on_commit(self, uow: UnitOfWork): ...
    def on_register(self, uow: UnitOfWork): ...

class RecordCommitOp:
    def __init__(
        self,
        record: Union[FileRecord, Record],
        indexer: Optional[RecordIndexer] = ...,
        index_refresh: bool = ...,
    ): ...
    def on_commit(self, uow: UnitOfWork): ...
    def on_register(self, uow: UnitOfWork): ...

class RecordDeleteOp:
    def __init__(
        self,
        record: Record,
        indexer: Optional[RecordIndexer] = ...,
        force: bool = ...,
        index_refresh: bool = ...,
    ): ...
    def on_commit(self, uow: UnitOfWork): ...
    def on_register(self, uow: UnitOfWork): ...

class TaskOp:
    def __init__(self, celery_task: Any, *args, **kwargs): ...
    def on_post_commit(self, uow: UnitOfWork): ...
