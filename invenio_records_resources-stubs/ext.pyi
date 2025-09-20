from typing import (
    Optional,
)

from flask.app import Flask

class InvenioRecordsResources:
    def __init__(self, app: Optional[Flask] = ...): ...
    def init_app(self, app: Flask): ...
    def init_config(self, app: Flask): ...
