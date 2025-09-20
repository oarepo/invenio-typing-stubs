import enum
from typing import Any, Dict, Optional

from invenio_communities.communities.records.api import Community
from invenio_records.systemfields import SystemField

class CommunityDeletionStatusEnum(enum.Enum):
    PUBLISHED = "P"
    DELETED = "D"
    MARKED = "X"

class CommunityDeletionStatus:
    _status: CommunityDeletionStatusEnum
    def __init__(
        self, status: Optional[CommunityDeletionStatusEnum] = None
    ) -> None: ...
    @property
    def status(self) -> CommunityDeletionStatusEnum: ...
    @status.setter
    def status(self, value: CommunityDeletionStatusEnum) -> None: ...
    @property
    def is_deleted(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...

class CommunityDeletionStatusField(SystemField[Community, CommunityDeletionStatus]):
    def pre_commit(self, record: Community) -> None: ...
    def pre_dump(
        self, record: Community, data: Dict[str, Any], **kwargs: Any
    ) -> None: ...
    def post_load(
        self, record: Community, data: Dict[str, Any], **kwargs: Any
    ) -> None: ...
