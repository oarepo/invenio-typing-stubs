from _typeshed import Incomplete
from invenio_audit_logs.proxies import (
    current_audit_logs_actions_registry as current_audit_logs_actions_registry,
)
from invenio_audit_logs.records import AuditLog as AuditLog
from invenio_audit_logs.services import results as results
from invenio_audit_logs.services.permissions import (
    AuditLogPermissionPolicy as AuditLogPermissionPolicy,
)
from invenio_audit_logs.services.schema import AuditLogSchema as AuditLogSchema
from invenio_indexer.api import RecordIndexer
from invenio_records_resources.services.base import ServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin
from invenio_records_resources.services.records.config import (
    SearchOptions as SearchOptionsBase,
)

class AuditLogSearchOptions(SearchOptionsBase):
    sort_default: str
    sort_default_no_query: str
    query_parser_cls: Incomplete
    sort_options: Incomplete
    facets: Incomplete
    pagination_options: Incomplete
    params_interpreters_cls: Incomplete

def idvar(log, vars) -> None: ...

class AuditLogServiceConfig(ServiceConfig, ConfiguratorMixin):
    enabled: Incomplete
    service_id: str
    permission_policy_cls: Incomplete
    search = AuditLogSearchOptions
    schema = AuditLogSchema
    record_cls = AuditLog
    indexer_cls = RecordIndexer
    indexer_queue_name = service_id
    index_dumper: Incomplete
    components: Incomplete
    links_item: Incomplete
    links_search: Incomplete
    result_item_cls: Incomplete
    result_list_cls: Incomplete
