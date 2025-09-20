from typing import Any, Dict, List, Tuple

from invenio_records_resources.resources.records.resource import (
    RecordResource,
    request_data,
    request_extra_args,
    request_search_args,
    request_view_args,
)

class MemberResource(RecordResource):
    def create_url_rules(self) -> List[Dict[str, Any]]: ...
    @request_view_args
    @request_search_args
    def search(self) -> Tuple[Dict[str, Any], int]: ...
    @request_view_args
    @request_search_args
    def search_public(self) -> Tuple[Dict[str, Any], int]: ...
    @request_view_args
    @request_search_args
    def search_invitations(self) -> Tuple[Dict[str, Any], int]: ...
    @request_view_args
    @request_data
    def add(self) -> Any: ...
    @request_view_args
    @request_data
    def invite(self) -> Any: ...
    @request_view_args
    @request_data
    def request_membership(self) -> Tuple[Dict[str, Any], int]: ...
    @request_view_args
    @request_extra_args
    @request_data
    def update(self) -> Any: ...
    @request_view_args
    @request_data
    def update_invitations(self) -> Any: ...
    @request_view_args
    @request_data
    def delete(self) -> Any: ...
