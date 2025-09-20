from typing import Dict

from invenio_records_resources.resources.records.resource import request_view_args
from invenio_vocabularies.contrib.names.names import record_type as record_type
from marshmallow import fields

class NamesResourceConfig(record_type.resource_config_cls):
    routes: Dict[str, str]
    request_view_args: Dict[str, fields.Field]

class NamesResource(record_type.resource_cls):
    def create_url_rules(self): ...
    @request_view_args
    def name_resolve_by_id(self): ...
