# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2024 CERN.
# Copyright (C) 2020-2025 Northwestern University.
# Copyright (C) 2023 Graz University of Technology.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Record Service API."""

from typing import Any, Callable, Mapping, Sequence

import marshmallow as ma
from invenio_indexer.api import RecordIndexer
from invenio_records.dumpers import Dumper
from invenio_records_resources.records import Record
from invenio_records_resources.services.base import ServiceConfig
from invenio_records_resources.services.base.links import Link
from invenio_records_resources.services.records.components.base import ServiceComponent
from invenio_records_resources.services.records.params import ParamInterpreter
from invenio_records_resources.services.records.queryparser import QueryParser
from invenio_search import RecordsSearchV2

class SearchOptions:
    """Search options."""

    # NOTE: configs expose immutable defaults so subclasses can override
    # without mutating shared state.
    search_cls: type[RecordsSearchV2]
    query_parser_cls: type[QueryParser]
    suggest_parser_cls: type[QueryParser] | None
    sort_default: str = "bestmatch"
    sort_default_no_query: str = "newest"
    sort_options: Mapping[str, Mapping[str, Any]]
    facets: Mapping[str, Any]
    pagination_options: Mapping[str, int]
    params_interpreters_cls: tuple[type[ParamInterpreter], ...]

class RecordServiceConfig(ServiceConfig):
    """Service factory configuration."""

    # Record specific configuration
    # NOTE: defaults are immutable here as well to prevent runtime mutation.
    record_cls: type[Record]
    indexer_cls: type[RecordIndexer]
    indexer_queue_name: str
    index_dumper: Dumper | None
    # inverse relation mapping, stores which fields relate to which record type
    relations: Mapping[str, Any]

    # Search configuration
    search: type[SearchOptions]

    # Service schema
    schema: type[ma.Schema] | None

    # Definition of those is left up to implementations

    @property
    def links_item(
        self,
    ) -> dict[
        str, Callable[..., Any] | Link
    ]: ...  # keep typing to be able to use property
    @property
    def links_search(
        self,
    ) -> dict[
        str, Callable[..., Any] | Link
    ]: ...  # keep typing to be able to use property
    @property
    def components(
        self,
    ) -> Sequence[type[ServiceComponent]]: ...  # keep typing to be able to use property
