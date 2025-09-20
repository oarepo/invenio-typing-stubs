from typing import Dict, Optional, Union

from flask_principal import Identity
from invenio_communities.communities.records.api import Community
from invenio_communities.members.records.api import Member
from invenio_communities.members.records.api import MemberMixin as MemberMixin
from invenio_records_resources.services.records.components import ServiceComponent

from ...proxies import current_identities_cache as current_identities_cache
from ...utils import on_group_membership_change as on_group_membership_change
from ...utils import on_user_membership_change as on_user_membership_change

class CommunityMemberCachingComponent(ServiceComponent):
    def _member_changed(
        self,
        member: Union[Member, Dict[str, str]],
        community: Optional[Community] = ...,
    ) -> None: ...
    def accept_invite(
        self,
        identity: Identity,
        record: Optional[Member] = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
    def members_add(
        self,
        identity: Identity,
        record: Optional[Dict[str, str]] = ...,
        community: Optional[Community] = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
    def members_delete(
        self,
        identity: Identity,
        record: Optional[Member] = ...,
        community: Optional[Community] = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
    def members_update(
        self,
        identity: Identity,
        record: Optional[Member] = ...,
        community: Optional[Community] = ...,
        data: None = ...,
        **kwargs,
    ) -> None: ...
