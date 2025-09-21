from typing import (
    Any,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

from invenio_search.engine import dsl
from opensearch_dsl.aggs import Terms
from opensearch_dsl.response.aggs import (
    FieldBucket,
    FieldBucketData,
)

class LabelledFacetMixin:
    def __init__(
        self,
        label: str | None = None,
        value_labels: dict[str, str] | None = None,
        **kwargs: Any,
    ): ...
    def get_value(self, bucket: FieldBucket) -> str: ...
    def get_label_mapping(self, buckets: list[FieldBucket]) -> Dict[str, str]: ...
    def get_values(self, data: Any, filter_values: List[Any]) -> Dict[str, Any]: ...
    def get_labelled_values(
        self, data: Any, filter_values: List[Any]
    ) -> Dict[str, Any]: ...

class TermsFacet(LabelledFacetMixin, dsl.TermsFacet): ...

class CombinedTermsFacet:
    def __init__(
        self,
        field: str,
        combined_field: str,
        parents: List[str],
        splitchar: str = ...,
        **kwargs,
    ): ...
    def get_aggregation(self) -> Terms: ...
    def get_labelled_values(
        self, data: FieldBucketData, filter_values: List[Any]
    ) -> Dict[str, Any]: ...
    def get_parents(self) -> List[str]: ...
    def get_value_filter(self, parsed_value: Any) -> Any: ...

class NestedTermsFacet:
    def __init__(
        self,
        field: Optional[str] = ...,
        subfield: Optional[str] = ...,
        splitchar: str = ...,
        **kwargs,
    ): ...
    def _parse_values(self, filter_values: List[str]) -> Dict[str, Any]: ...
    def add_filter(self, filter_values: List[str]) -> Any: ...
    def get_aggregation(self) -> Terms: ...
    def get_labelled_values(
        self,
        data: FieldBucketData,
        filter_values: List[Any],
        bucket_label: bool = ...,
        key_prefix: Optional[str] = ...,
    ) -> Dict[str, Any]: ...
    def get_value_filter(
        self, parsed_value: Union[Tuple[str, List[Any]], Tuple[str, List[str]]]
    ) -> Any: ...

class CFFacetMixin:
    @classmethod
    def field(cls, field: str) -> str: ...

class CFTermsFacet(CFFacetMixin, TermsFacet):
    def __init__(
        self,
        *,
        field: str,
        label: str | None = None,
        value_labels: dict[str, str] | None = None,
        **kwargs: Any,
    ): ...

class CFNestedTermsFacet(CFFacetMixin, NestedTermsFacet):
    def __init__(
        self,
        *,
        field: str,
        label: str | None = None,
        value_labels: dict[str, str] | None = None,
        **kwargs: Any,
    ): ...
