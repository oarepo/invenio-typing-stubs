from typing import Any, Dict, Optional

from _typeshed import Incomplete
from invenio_records_resources.resources import RecordResourceConfig

class RequestCommentsResourceConfig(RecordResourceConfig):
    blueprint_name: Optional[str]
    url_prefix: str
    routes: Dict[str, str]
    request_list_view_args: Dict[str, Any]
    request_item_view_args: Dict[str, Any]
    response_handlers: Dict[str, Incomplete]
