from typing import Any, Type

from sqlalchemy.ext.declarative import declared_attr

from ...communities.records.models import CommunityMetadata as CommunityMetadata

class CommunityRelationMixin:
    __record_model__: Type[Any]
    __request_model__: Type[Any]
    @declared_attr
    def community_id(cls): ...
    @declared_attr
    def record_id(cls): ...
    @declared_attr
    def request_id(cls): ...
