from typing import Any, List

from invenio_communities.notifications.generators import (
    CommunityMembersRecipient as CommunityMembersRecipient,
)
from invenio_notifications.models import Notification
from invenio_notifications.services.builders import NotificationBuilder

class BaseNotificationBuilder(NotificationBuilder):
    context: List[Any]  # List of EntityResolve objects
    recipient_filters: List[Any]  # List of filter objects
    recipient_backends: List[Any]  # List of backend objects

class CommunityInvitationNotificationBuilder(BaseNotificationBuilder): ...

class CommunityInvitationSubmittedNotificationBuilder(
    CommunityInvitationNotificationBuilder
):
    type: str
    @classmethod
    def build(cls, **kwargs) -> Notification: ...
    recipients: List[Any]  # List of UserRecipient objects

class CommunityInvitationAcceptNotificationBuilder(
    CommunityInvitationNotificationBuilder
):
    type: str
    @classmethod
    def build(cls, **kwargs) -> Notification: ...
    recipients: List[Any]  # List of CommunityMembersRecipient objects

class CommunityInvitationCancelNotificationBuilder(
    CommunityInvitationNotificationBuilder
):
    type: str
    @classmethod
    def build(cls, **kwargs) -> Notification: ...
    recipients: List[Any]  # List of UserRecipient objects

class CommunityInvitationDeclineNotificationBuilder(
    CommunityInvitationNotificationBuilder
):
    type: str
    @classmethod
    def build(cls, **kwargs) -> Notification: ...
    recipients: List[Any]  # List of CommunityMembersRecipient objects

class CommunityInvitationExpireNotificationBuilder(
    CommunityInvitationNotificationBuilder
):
    type: str
    @classmethod
    def build(cls, **kwargs) -> Notification: ...
    recipients: List[Any]  # List of UserRecipient objects

class SubCommunityBuilderBase(BaseNotificationBuilder):
    type: str
    context: List[Any]  # List of EntityResolve objects
    @classmethod
    def build(cls, **kwargs) -> Notification: ...
    recipients: List[Any]  # List of recipient objects
    recipient_filters: List[Any]  # List of filter objects

class SubCommunityCreate(SubCommunityBuilderBase):
    type: str
    recipient_filters: List[Any]  # List of filter objects

class SubCommunityAccept(SubCommunityBuilderBase):
    type: str

class SubCommunityDecline(SubCommunityBuilderBase):
    type: str

class SubComInvitationBuilderBase(SubCommunityBuilderBase):
    type: str
    context: List[Any]  # List of EntityResolve objects

class SubComInvitationCreate(SubComInvitationBuilderBase):
    type: str
    context: List[Any]  # List of EntityResolve objects
    recipients: List[Any]  # List of recipient objects

class SubComInvitationAccept(SubComInvitationBuilderBase):
    type: str
    recipient_filters: List[Any]  # List of filter objects

class SubComInvitationDecline(SubComInvitationBuilderBase):
    type: str
    recipient_filters: List[Any]  # List of filter objects

class SubComInvitationExpire(SubComInvitationBuilderBase):
    type: str
    context: List[Any]  # List of EntityResolve objects
    recipients: List[Any]  # List of recipient objects

class SubComCommentNotificationBuilderBase(SubCommunityBuilderBase):
    context: List[Any]  # List of EntityResolve objects
    @classmethod
    def build(cls, **kwargs): ...
    recipient_filters: List[Any]  # List of filter objects

class SubComReqCommentNotificationBuilder(SubComCommentNotificationBuilderBase):
    type: str

class SubComInvCommentNotificationBuilder(SubComCommentNotificationBuilderBase):
    type: str
