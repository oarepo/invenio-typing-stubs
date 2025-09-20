from typing import Any, Callable

from _typeshed import Incomplete
from invenio_drafts_resources.records.api import Draft
from invenio_drafts_resources.services.records.components import (
    DraftMetadataComponent as DraftMetadataComponent,
)
from invenio_drafts_resources.services.records.components import (
    PIDComponent as PIDComponent,
)
from invenio_drafts_resources.services.records.permissions import (
    RecordPermissionPolicy as RecordPermissionPolicy,
)
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as ParentSchema,
)
from invenio_drafts_resources.services.records.schema import (
    RecordSchema as RecordSchema,
)
from invenio_drafts_resources.services.records.search_params import (
    AllVersionsParam as AllVersionsParam,
)
from invenio_indexer.api import RecordIndexer
from invenio_records_resources.services import (
    RecordServiceConfig as RecordServiceConfigBase,
)
from invenio_records_resources.services import SearchOptions as SearchOptionsBase

def is_draft(record, ctx): ...
def is_record(record, ctx): ...
def lock_edit_published_files(service, identity, record=None, draft=None): ...

class SearchOptions(SearchOptionsBase):
    sort_options: Incomplete
    params_interpreters_cls: Incomplete

class SearchDraftsOptions(SearchOptions):
    sort_default: str
    sort_default_no_query: str
    sort_options: Incomplete
    params_interpreters_cls: Incomplete

class SearchVersionsOptions(SearchOptions):
    sort_default: str
    sort_default_no_query: str
    sort_options: Incomplete
    facets_options: Incomplete
    params_interpreters_cls: Incomplete

class RecordServiceConfig(RecordServiceConfigBase):
    draft_cls: type[Draft]
    draft_indexer_cls: type[RecordIndexer]
    draft_indexer_queue_name: Incomplete
    schema_parent: type[ParentSchema]
    search_drafts: type[SearchDraftsOptions]
    search_versions: type[SearchVersionsOptions]
    default_files_enabled: bool
    default_media_files_enabled: bool
    lock_edit_published_files: Callable[..., Any]
    links_item: Incomplete
    links_search: Incomplete
    links_search_drafts: Incomplete
    links_search_versions: Incomplete
