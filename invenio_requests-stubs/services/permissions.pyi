from typing import Sequence

from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import Generator
from invenio_requests.services.generators import Commenter as Commenter
from invenio_requests.services.generators import Creator as Creator
from invenio_requests.services.generators import Receiver as Receiver
from invenio_requests.services.generators import Reviewers as Reviewers
from invenio_requests.services.generators import Status as Status
from invenio_requests.services.generators import Topic as Topic

class PermissionPolicy(RecordPermissionPolicy):
    can_create: Sequence[Generator]
    can_search: Sequence[Generator]
    can_search_user_requests = can_search
    can_read: Sequence[Generator]
    can_update: Sequence[Generator]
    can_manage_access_options: Sequence[Generator]
    can_action_delete: Sequence[Generator]
    can_action_submit: Sequence[Generator]
    can_action_cancel: Sequence[Generator]
    can_action_expire: Sequence[Generator]
    can_action_accept: Sequence[Generator]
    can_action_decline: Sequence[Generator]
    can_update_comment: Sequence[Generator]
    can_delete_comment: Sequence[Generator]
    can_create_comment = can_read
    can_unused: Sequence[Generator]
