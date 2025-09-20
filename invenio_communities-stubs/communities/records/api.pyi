from typing import Any, Optional, Type

from invenio_communities.communities.records import models as models
from invenio_communities.communities.records.systemfields.access import (
    CommunityAccessField as CommunityAccessField,
)
from invenio_communities.communities.records.systemfields.children import (
    ChildrenField as ChildrenField,
)
from invenio_communities.communities.records.systemfields.deletion_status import (
    CommunityDeletionStatusField as CommunityDeletionStatusField,
)
from invenio_communities.communities.records.systemfields.is_verified import (
    IsVerifiedField as IsVerifiedField,
)
from invenio_communities.communities.records.systemfields.parent_community import (
    ParentCommunityField as ParentCommunityField,
)
from invenio_communities.communities.records.systemfields.pidslug import (
    PIDSlugField as PIDSlugField,
)
from invenio_communities.communities.records.systemfields.tombstone import (
    TombstoneField as TombstoneField,
)
from invenio_records_resources.records.api import FileRecord, Record

class CommunityFile(FileRecord):
    model_cls: Optional[Type[Any]]
    record_cls: Optional[Type[Any]]

class Community(Record):
    id: Any
    slug: Any
    pid: PIDSlugField
    parent: ParentCommunityField
    children: ChildrenField
    schema: Any
    model_cls: Optional[Type[Any]]
    dumper: Any
    index: Any
    access: CommunityAccessField
    custom_fields: Any
    theme: Any
    bucket_id: Any
    bucket: Any
    files: Any
    relations: Any
    is_verified: IsVerifiedField
    deletion_status: CommunityDeletionStatusField
    tombstone: TombstoneField
