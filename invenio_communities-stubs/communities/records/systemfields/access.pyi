from enum import Enum
from typing import Any, Dict, Optional, Type

from invenio_communities.communities.records.api import Community
from invenio_records.systemfields import SystemField

class AccessEnumMixin:
    def __str__(self) -> str: ...
    @classmethod
    def validate(cls, level: Any) -> bool: ...

class VisibilityEnum(AccessEnumMixin, Enum):
    PUBLIC = "public"
    RESTRICTED = "restricted"

class MembersVisibilityEnum(AccessEnumMixin, Enum):
    PUBLIC = "public"
    RESTRICTED = "restricted"

class MemberPolicyEnum(AccessEnumMixin, Enum):
    OPEN = "open"
    CLOSED = "closed"

class RecordSubmissionPolicyEnum(AccessEnumMixin, Enum):
    OPEN = "open"
    CLOSED = "closed"

class ReviewPolicyEnum(AccessEnumMixin, Enum):
    OPEN = "open"
    CLOSED = "closed"
    MEMBERS = "members"

class CommunityAccess:
    errors: list[str]
    def __init__(
        self,
        visibility: Optional[str] = None,
        members_visibility: Optional[str] = None,
        member_policy: Optional[str] = None,
        record_submission_policy: Optional[str] = None,
        review_policy: Optional[str] = None,
    ) -> None: ...
    @classmethod
    def validate_visibility_level(cls, level: str) -> bool: ...
    @classmethod
    def validate_members_visibility_level(cls, level: str) -> bool: ...
    @classmethod
    def validate_member_policy_level(cls, level: str) -> bool: ...
    @classmethod
    def validate_record_submission_policy_level(cls, level: str) -> bool: ...
    @classmethod
    def validate_review_policy_level(cls, level: str) -> bool: ...
    @property
    def visibility(self) -> str: ...
    @visibility.setter
    def visibility(self, value: str) -> None: ...
    @property
    def members_visibility(self) -> str: ...
    @members_visibility.setter
    def members_visibility(self, value: str) -> None: ...
    @property
    def visibility_is_public(self) -> bool: ...
    @property
    def visibility_is_restricted(self) -> bool: ...
    @property
    def member_policy(self) -> str: ...
    @member_policy.setter
    def member_policy(self, value: str) -> None: ...
    @property
    def record_submission_policy(self) -> str: ...
    @record_submission_policy.setter
    def record_submission_policy(self, value: str) -> None: ...
    @property
    def review_policy(self) -> str: ...
    @review_policy.setter
    def review_policy(self, value: str) -> None: ...
    def dump(self) -> Dict[str, str]: ...
    def refresh_from_dict(self, access_dict: Dict[str, str]) -> None: ...
    @classmethod
    def from_dict(cls, access_dict: Dict[str, str]) -> CommunityAccess: ...

class CommunityAccessField(SystemField[Community, CommunityAccess]):
    access_obj_class = CommunityAccess
    def __init__(
        self,
        key: str = "access",
        access_obj_class: Optional[Type[CommunityAccess]] = None,
    ) -> None: ...
    def obj(self, instance: Community) -> CommunityAccess: ...
    def set_obj(self, record: Community, obj: CommunityAccess) -> None: ...
    def pre_commit(self, record: Community) -> None: ...
