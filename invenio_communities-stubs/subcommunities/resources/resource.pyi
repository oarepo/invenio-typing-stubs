from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from flask_resources import Resource
from invenio_records_resources.resources.records.resource import (
    request_data,
    request_view_args,
)

class SubCommunityResource(Resource):
    service: Any
    def __init__(self, config, service) -> None: ...
    def create_url_rules(
        self,
    ) -> List[Dict[str, Optional[Union[str, List[str], Callable]]]]: ...
    @request_view_args
    @request_data
    def join(self) -> Tuple[Dict[str, Any], int]: ...
