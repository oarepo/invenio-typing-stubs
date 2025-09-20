from typing import Any, Optional, Type

from invenio_communities.records.records.systemfields.communities.context import (
    CommunitiesFieldContext as CommunitiesFieldContext,
)
from invenio_communities.records.records.systemfields.communities.manager import (
    CommunitiesRelationManager as CommunitiesRelationManager,
)
from invenio_records.systemfields import SystemField

class CommunitiesField(SystemField):
    def __init__(
        self,
        m2m_model_cls: Type[Any],
        key: str = "communities",
        context_cls: Optional[Type[Any]] = None,
        manager_cls: Optional[Type[Any]] = None,
    ) -> None: ...
    def pre_commit(self, record: Any) -> None: ...
    def obj(self, record: Any) -> CommunitiesRelationManager: ...
    def __get__(self, record: Any, owner: Type[Any]) -> Any: ...
    def post_dump(
        self, record: Any, data: Any, dumper: Optional[Any] = None
    ) -> None: ...
    def post_load(
        self, record: Any, data: Any, loader: Optional[Any] = None
    ) -> None: ...
