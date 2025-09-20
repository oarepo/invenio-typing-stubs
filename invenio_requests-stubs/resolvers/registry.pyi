from typing import Any, Iterator

from invenio_records_resources.references.registry import ResolverRegistryBase
from invenio_requests.proxies import current_requests as current_requests

class ResolverRegistry(ResolverRegistryBase):
    @classmethod
    def get_registered_resolvers(cls) -> Iterator[Any]: ...
