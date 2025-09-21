from typing import Any, Dict

from invenio_records_permissions.policies.records import (
    RecordPermissionPolicy as RecordPermissionPolicy,
)
from invenio_records_resources.services import Link, RecordServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_records_resources.services.records.results import RecordItem, RecordList
from invenio_requests.records.api import Request as Request
from invenio_requests.records.api import RequestEvent as RequestEvent
from marshmallow import Schema

class RequestEventItem(RecordItem):
    @property
    def id(self) -> str: ...

class RequestEventList(RecordList): ...

class RequestEventLink(Link):
    @staticmethod
    def vars(record: RequestEvent, vars: Dict[str, Any]) -> None: ...

class RequestEventsServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    request_cls = Request
    permission_policy_cls: type[RecordPermissionPolicy]
    schema: type[Schema]
    record_cls = RequestEvent
    result_item_cls: type[RequestEventItem]  # type: ignore[assignment]
    result_list_cls: type[RequestEventList]  # type: ignore[assignment]
    indexer_queue_name: str
