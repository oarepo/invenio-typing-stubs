from typing import Optional

from flask.app import Flask
from invenio_records_resources.registry import NotificationRegistry, ServiceRegistry
from invenio_records_resources.services.files.transfer.registry import (
    TransferRegistry,
)

class InvenioRecordsResources:
    app: Flask
    registry: ServiceRegistry
    notification_registry: NotificationRegistry

    def __init__(self, app: Optional[Flask] = ...): ...
    def init_app(self, app: Flask) -> None: ...
    def init_config(self, app: Flask) -> None: ...
    @property
    def transfer_registry(self) -> TransferRegistry: ...
