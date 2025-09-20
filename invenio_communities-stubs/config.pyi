from typing import Any

from invenio_communities.communities.records.systemfields.access import (
    RecordSubmissionPolicyEnum as RecordSubmissionPolicyEnum,
)
from invenio_communities.communities.services import facets as facets

COMMUNITIES_ROUTES: dict[str, str]
COMMUNITIES_FACETS: dict[str, dict[str, Any]]
COMMUNITIES_SUBCOMMUNITIES_FACETS = COMMUNITIES_FACETS
COMMUNITIES_SORT_OPTIONS: dict[str, dict[str, Any]]
COMMUNITIES_ROLES: list[dict[str, Any]]
COMMUNITIES_SEARCH: dict[str, Any]
COMMUNITIES_SEARCH_SORT_BY_VERIFIED: bool
COMMUNITIES_SUBCOMMUNITIES_SEARCH: dict[str, Any]
COMMUNITIES_REQUESTS_SEARCH: dict[str, Any]
COMMUNITIES_MEMBERS_SEARCH: dict[str, Any]
COMMUNITIES_MEMBERS_SORT_OPTIONS: dict[str, dict[str, Any]]
COMMUNITIES_MEMBERS_FACETS: dict[str, dict[str, Any]]
COMMUNITIES_INVITATIONS_SEARCH: dict[str, Any]
COMMUNITIES_INVITATIONS_SORT_OPTIONS: dict[str, dict[str, Any]]
COMMUNITIES_INVITATIONS_EXPIRES_IN: int  # timedelta.days converted to int
COMMUNITIES_LOGO_MAX_FILE_SIZE: int
COMMUNITIES_NAMESPACES: list[str]
COMMUNITIES_CUSTOM_FIELDS: dict[str, Any]
COMMUNITIES_CUSTOM_FIELDS_UI: dict[str, Any]
COMMUNITIES_ALLOW_RESTRICTED: bool
COMMUNITIES_IDENTITIES_CACHE_TIME: int  # timedelta.total_seconds() converted to int
COMMUNITIES_IDENTITIES_CACHE_REDIS_URL: str
COMMUNITIES_IDENTITIES_CACHE_HANDLER: str
COMMUNITIES_OAI_SETS_PREFIX: str
COMMUNITIES_ALWAYS_SHOW_CREATE_LINK: bool
COMMUNITIES_ALLOW_MEMBERSHIP_REQUESTS: bool
COMMUNITIES_DEFAULT_RECORD_SUBMISSION_POLICY: str  # RecordSubmissionPolicyEnum value
