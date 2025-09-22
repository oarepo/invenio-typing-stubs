# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2020-2024 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Record type factory."""

from typing import ClassVar

import marshmallow as ma
from _typeshed import Incomplete
from invenio_records.dumpers import SearchDumper
from invenio_records.models import RecordMetadataBase
from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields.pid import PIDField
from invenio_records_resources.resources import (
    RecordResource,
    RecordResourceConfig,
)
from invenio_records_resources.services import RecordService, RecordServiceConfig
from invenio_records_resources.services.records.config import SearchOptions

class RecordTypeFactory:
    """Factory of record types."""

    # Class attributes populated during creation
    model_cls: ClassVar[type[RecordMetadataBase] | None]
    record_cls: ClassVar[type[Record] | None]
    resource_cls: ClassVar[type[RecordResource] | None]
    resource_config_cls: ClassVar[type[RecordResourceConfig] | None]
    service_config_cls: ClassVar[type[RecordServiceConfig] | None]
    service_cls: ClassVar[type[RecordService] | None]

    _schema_path_template: ClassVar[str]
    _index_name_template: ClassVar[str]

    # Instance attributes set in constructor
    record_type_name: str
    record_name_lower: str
    name_plural: str
    pid_field_cls: type[PIDField]
    pid_field_kwargs: dict[str, Incomplete]
    schema_version: str
    record_dumper: SearchDumper | None
    record_relations: Incomplete | None
    schema_path: str
    index_name: str
    model_cls_attrs: dict[str, Incomplete]
    record_cls_attrs: dict[str, Incomplete]
    resource_cls_attrs: dict[str, Incomplete]
    endpoint_route: str | None
    service_id: str | None
    service_schema: type[ma.Schema]
    search_options: type[SearchOptions] | SearchOptions
    service_components: list[type[Incomplete]] | None
    permission_policy_cls: type[RecordPermissionPolicy] | None

    # Constructor
    def __init__(
        self,
        record_type_name: str,
        service_schema: type[ma.Schema],
        schema_version: str = "1.0.0",
        endpoint_route: str | None = None,
        record_dumper: SearchDumper | None = None,
        record_relations: Incomplete | None = None,
        schema_path: str | None = None,
        index_name: str | None = None,
        search_options: type[SearchOptions] | SearchOptions | None = None,
        service_components: list[type[Incomplete]] | None = None,
        permission_policy_cls: type[RecordPermissionPolicy] | None = None,
        pid_field_cls: type[PIDField] = PIDField,
        pid_field_kwargs: dict[str, Incomplete] | None = None,
        model_cls_attrs: dict[str, Incomplete] | None = None,
        record_cls_attrs: dict[str, Incomplete] | None = None,
        resource_cls_attrs: dict[str, Incomplete] | None = None,
        service_id: str | None = None,
    ) -> None: ...

    # Helpers
    def _build_index_name(self, index_name: str | None) -> str: ...
    def _build_schema_path(self, optional_schema_path: str | None) -> str: ...

    # Factory steps
    def create_metadata_model(self) -> None: ...
    def create_record_class(self) -> None: ...
    def create_resource_class(self) -> None: ...
    def create_service_class(self) -> None: ...
    def create_record_type(self) -> None: ...
    def validate(self) -> None: ...
