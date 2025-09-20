from typing import Callable

from invenio_communities.communities.resources.serializer import (
    UICommunityJSONSerializer as UICommunityJSONSerializer,
)
from invenio_communities.proxies import current_communities as current_communities

def pass_community(serialize: bool) -> Callable: ...
def warn_deprecation(deprecated_route: str, new_route: str) -> Callable: ...
