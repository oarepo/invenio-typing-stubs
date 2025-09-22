# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2023 Northwestern University.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Facets types defined."""

from collections.abc import Iterable
from typing import Any, Callable

from invenio_search.engine import dsl  # type: ignore[import-untyped]
from opensearch_dsl.response.aggs import FieldBucket, FieldBucketData

class LabelledFacetMixin:
    """Mixin class for overwriting the default get_values() method."""

    def __init__(
        self,
        label: str | None = None,
        value_labels: (
            dict[str, str] | Callable[[list[str]], dict[str, str]] | None
        ) = None,
        **kwargs: Any,
    ) -> None: ...
    def get_value(self, bucket: FieldBucket) -> str: ...
    def get_label_mapping(self, buckets: list[FieldBucket]) -> dict[str, str]: ...
    def get_labelled_values(
        self, data: Any, filter_values: list[Any]
    ) -> dict[str, Any]: ...

class TermsFacet(LabelledFacetMixin, dsl.TermsFacet):
    pass

class CombinedTermsFacet(NestedTermsFacet):
    def __init__(
        self,
        field: str,
        combined_field: str,
        parents: Iterable[str] | Callable[[], Iterable[str]],
        splitchar: str = "::",
        **kwargs: Any,
    ) -> None: ...
    def get_aggregation(self) -> Any: ...
    def get_labelled_values(
        self,
        data: FieldBucketData,
        filter_values: list[Any],
        bucket_label: bool = ...,
        key_prefix: str | None = ...,
    ) -> dict[str, Any]: ...
    def get_parents(self) -> Iterable[str]: ...
    def get_value_filter(self, parsed_value: Any) -> Any: ...

class NestedTermsFacet:
    def __init__(
        self,
        field: str | None = None,
        subfield: str | None = None,
        splitchar: str = "::",
        **kwargs: Any,
    ) -> None: ...
    def _parse_values(self, filter_values: list[str]) -> dict[str, Any]: ...
    def add_filter(self, filter_values: list[str]) -> Any: ...
    def get_aggregation(self) -> Any: ...
    def get_labelled_values(
        self,
        data: FieldBucketData,
        filter_values: list[Any],
        bucket_label: bool = True,
        key_prefix: str | None = None,
    ) -> dict[str, Any]: ...
    def get_value_filter(
        self, parsed_value: tuple[str, list[Any]] | tuple[str, list[str]]
    ) -> Any: ...

class CFFacetMixin:
    @classmethod
    def field(cls, field: str) -> str: ...

class CFTermsFacet(CFFacetMixin, TermsFacet):
    def __init__(
        self,
        field: str | None = None,
        label: str | None = None,
        value_labels: (
            dict[str, str] | Callable[[list[str]], dict[str, str]] | None
        ) = None,
        **kwargs: Any,
    ) -> None: ...

class CFNestedTermsFacet(CFFacetMixin, NestedTermsFacet):
    def __init__(
        self,
        field: str | None = None,
        label: str | None = None,
        value_labels: (
            dict[str, str] | Callable[[list[str]], dict[str, str]] | None
        ) = None,
        **kwargs: Any,
    ) -> None: ...
