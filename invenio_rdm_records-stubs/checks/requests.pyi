from __future__ import annotations

from typing import Any

from flask_principal import Identity

class SubmissionCreateAction:
    def execute(self, identity: Identity, uow: Any) -> None: ...

class SubmissionCancelAction:
    def execute(self, identity: Identity, uow: Any) -> None: ...

class CommunitySubmission:
    available_actions: dict[str, type]

class InclusionSubmitAction:
    def execute(self, identity: Identity, uow: Any) -> None: ...

class InclusionCancelAction:
    def execute(self, identity: Identity, uow: Any) -> None: ...

class CommunityInclusion:
    available_actions: dict[str, type]
