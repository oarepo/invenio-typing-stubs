from typing import (
    Type,
)

from invenio_records_resources.services.records.config import SearchOptions

class ParamInterpreter:
    def __init__(self, config: Type[SearchOptions]): ...
