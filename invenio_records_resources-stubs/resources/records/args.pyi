from typing import (
    Any,
    Dict,
    Optional,
)

from flask_resources import MultiDictSchema
from marshmallow import fields
from werkzeug.datastructures.structures import ImmutableMultiDict

class SearchRequestArgsSchema(MultiDictSchema):

    q: fields.String
    suggest: fields.String
    sort: fields.String
    page: fields.Int
    size: fields.Int

    def facets(
        self,
        data: Dict[str, Any],
        original_data: Optional[ImmutableMultiDict] = ...,
        **kwargs,
    ) -> Dict[str, Any]: ...
