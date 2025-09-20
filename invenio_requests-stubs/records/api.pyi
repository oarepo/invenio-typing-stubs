from enum import Enum
from typing import Any, Callable

from invenio_records.dumpers import SearchDumper
from invenio_records.systemfields import ConstantField, DictField, ModelField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.entity_reference import (
    MultiReferenceEntityField,
    ReferencedEntityField,
)
from invenio_requests.records.dumpers import (
    CalculatedFieldDumperExt as CalculatedFieldDumperExt,
)
from invenio_requests.records.dumpers import (
    GrantTokensDumperExt as GrantTokensDumperExt,
)
from invenio_requests.records.models import RequestEventModel as RequestEventModel
from invenio_requests.records.models import RequestMetadata as RequestMetadata
from invenio_requests.records.systemfields import (
    EntityReferenceField as EntityReferenceField,
)
from invenio_requests.records.systemfields import EventTypeField as EventTypeField
from invenio_requests.records.systemfields import (
    ExpiredStateCalculatedField as ExpiredStateCalculatedField,
)
from invenio_requests.records.systemfields import IdentityField as IdentityField
from invenio_requests.records.systemfields import (
    RequestStateCalculatedField as RequestStateCalculatedField,
)
from invenio_requests.records.systemfields import (
    RequestStatusField as RequestStatusField,
)
from invenio_requests.records.systemfields import RequestTypeField as RequestTypeField
from invenio_requests.records.systemfields.entity_reference import (
    MultiEntityReferenceField as MultiEntityReferenceField,
)
from invenio_requests.records.systemfields.entity_reference import (
    check_allowed_creators as check_allowed_creators,
)
from invenio_requests.records.systemfields.entity_reference import (
    check_allowed_receivers as check_allowed_receivers,
)
from invenio_requests.records.systemfields.entity_reference import (
    check_allowed_reviewers as check_allowed_reviewers,
)
from invenio_requests.records.systemfields.entity_reference import (
    check_allowed_topics as check_allowed_topics,
)

class Request(Record):
    model_cls = RequestMetadata
    dumper: SearchDumper
    number: IdentityField
    metadata: None
    index: IndexField
    schema: ConstantField
    type: RequestTypeField
    topic: ReferencedEntityField
    created_by: ReferencedEntityField
    receiver: ReferencedEntityField
    reviewers: MultiReferenceEntityField
    status: RequestStatusField
    is_closed: RequestStateCalculatedField
    is_open: RequestStateCalculatedField
    expires_at: ModelField
    is_expired: ExpiredStateCalculatedField

class RequestEventFormat(Enum):
    HTML = "html"

class RequestEvent(Record):
    model_cls = RequestEventModel
    metadata: None
    schema: ConstantField
    request: ModelField
    request_id: DictField
    type: EventTypeField
    index: IndexField
    id: ModelField
    check_referenced: Callable[..., Any]
    created_by: ReferencedEntityField
