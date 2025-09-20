from typing import Any, Type

from flask_principal import Identity
from invenio_communities.proxies import current_communities as current_communities
from invenio_db.uow import UnitOfWork
from invenio_files_rest.app import Flask
from invenio_i18n.babel import LazyString
from invenio_requests.customizations import RequestType, actions

# Note: Builders are used only as types; keep them as Any to avoid import issues in stubs
SubComInvCommentNotificationBuilder: type[Any]
SubComReqCommentNotificationBuilder: type[Any]

class AcceptSubcommunity(actions.AcceptAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class DeclineSubcommunity(actions.DeclineAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class SubCommunityRequest(RequestType):
    type_id: str
    name: LazyString
    creator_can_be_none: bool
    topic_can_be_none: bool
    allowed_creator_ref_types: list[str]
    allowed_receiver_ref_types: list[str]
    allowed_topic_ref_types: list[str]
    comment_notification_builder: type[Any]
    available_actions: dict[str, type]
    needs_context: str | None

class CreateSubcommunityInvitation(actions.CreateAndSubmitAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class AcceptSubcommunityInvitation(actions.AcceptAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class DeclineSubcommunityInvitation(actions.DeclineAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class SubCommunityInvitationRequest(RequestType):
    type_id: str
    name: LazyString
    creator_can_be_none: bool
    topic_can_be_none: bool
    allowed_creator_ref_types: list[str]
    allowed_receiver_ref_types: list[str]
    allowed_topic_ref_types: list[str]
    comment_notification_builder: type[Any]
    available_actions: dict[str, type]
    needs_context: str | None

def subcommunity_request_type(app: Flask) -> Type[SubCommunityRequest]: ...
def subcommunity_invitation_request_type(
    app: Flask,
) -> Type[SubCommunityInvitationRequest]: ...
