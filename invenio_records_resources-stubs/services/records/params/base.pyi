# Copyright (C) 2020-2024 CERN.
# Copyright (C) 2020-2024 Northwestern University.
# Copyright (C) 2021-2024 TU Wien.
# Copyright (C) 2023-2024 Graz University of Technology.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

from __future__ import annotations

from typing import Mapping

from _typeshed import Incomplete
from invenio_records_resources.services.records.config import SearchOptions

class ParamInterpreter:
    config: type[SearchOptions]
    def __init__(self, config: type[SearchOptions]) -> None: ...
    def apply(
        self, identity: Incomplete, search: Incomplete, params: Mapping[str, Incomplete]
    ) -> Incomplete: ...
