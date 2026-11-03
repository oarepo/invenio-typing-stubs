from __future__ import annotations

from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_rdm_records.requests import community_inclusion, community_submission
from invenio_requests.customizations.actions import RequestAction

# At runtime these are looked up from the parent types' available_actions dicts, so
# only the dict's value contract is declared; the concrete classes may change upstream.
BaseCommunitySubmissionCreateAction: type[RequestAction]
BaseCommunitySubmissionCancelAction: type[RequestAction]
BaseCommunityInclussionSubmitAction: type[RequestAction]
BaseCommunityInclusionCancelAction: type[RequestAction]

class SubmissionCreateAction(RequestAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class SubmissionCancelAction(RequestAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class CommunitySubmission(community_submission.CommunitySubmission): ...

class InclusionSubmitAction(community_inclusion.SubmitAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class InclusionCancelAction(RequestAction):
    def execute(self, identity: Identity, uow: UnitOfWork) -> None: ...

class CommunityInclusion(community_inclusion.CommunityInclusion): ...
