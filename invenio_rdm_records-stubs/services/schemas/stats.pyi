from __future__ import annotations

from marshmallow import Schema

class PartialStatsSchema(Schema):
    views: Any
    unique_views: Any
    downloads: Any
    unique_downloads: Any
    data_volume: Any

class StatsSchema(Schema):
    this_version: Any
    all_versions: Any
