from functools import partial
from typing import (
    Any,
    List,
    Optional,
    Set,
    Type,
)

from flask_principal import (
    Identity,
)
from invenio_records_resources.services.records.queryparser.transformer import (
    SearchFieldTransformer,
)

class QueryParser:
    def __init__(
        self,
        identity: Optional[Identity] = ...,
        extra_params: Optional[Any] = ...,
        tree_transformer_cls: Optional[Type[SearchFieldTransformer]] = ...,
    ): ...
    @property
    def allow_list(self) -> Set[str]: ...
    @classmethod
    def factory(
        cls,
        tree_transformer_cls: Optional[Type[SearchFieldTransformer]] = ...,
        **extra_params,
    ) -> partial: ...
    @property
    def fields(self) -> List[Any]: ...
    def parse(self, query_str: str) -> Any: ...
