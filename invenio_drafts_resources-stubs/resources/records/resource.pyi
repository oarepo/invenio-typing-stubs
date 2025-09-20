from flask_resources import JSONSerializer as JSONSerializer
from flask_resources import ResponseHandler as ResponseHandler
from invenio_drafts_resources.resources.records.errors import (
    RedirectException as RedirectException,
)
from invenio_records_resources.resources import RecordResource as RecordResourceBase
from invenio_records_resources.resources.records.headers import (
    etag_headers as etag_headers,
)
from invenio_records_resources.resources.records.resource import (
    request_data,
    request_extra_args,
    request_headers,
    request_read_args,
    request_search_args,
    request_view_args,
)

class RecordResource(RecordResourceBase):
    def create_blueprint(self, **options): ...
    def create_url_rules(self): ...
    @request_extra_args
    @request_search_args
    @request_view_args
    def search_user_records(self): ...
    @request_extra_args
    @request_search_args
    @request_view_args
    def search_versions(self): ...
    @request_extra_args
    @request_view_args
    def new_version(self): ...
    @request_extra_args
    @request_view_args
    def edit(self): ...
    @request_extra_args
    @request_view_args
    def publish(self): ...
    @request_view_args
    def import_files(self): ...
    @request_extra_args
    @request_view_args
    def read_latest(self) -> None: ...
    @request_extra_args
    @request_read_args
    @request_view_args
    def read_draft(self): ...
    @request_extra_args
    @request_headers
    @request_view_args
    @request_data
    def update_draft(self): ...
    @request_headers
    @request_view_args
    def delete_draft(self): ...
