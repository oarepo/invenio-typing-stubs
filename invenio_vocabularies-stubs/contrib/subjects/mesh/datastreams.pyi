from typing import Any, Dict, Type

from invenio_vocabularies.datastreams.transformers import (
    BaseTransformer as BaseTransformer,
)
from invenio_vocabularies.datastreams.transformers import (
    TransformerError as TransformerError,
)

class MeshSubjectsTransformer(BaseTransformer):
    def apply(self, stream_entry, *args, **kwargs): ...

VOCABULARIES_DATASTREAM_READERS: Dict[str, Type[Any]]
VOCABULARIES_DATASTREAM_WRITERS: Dict[str, Type[Any]]
VOCABULARIES_DATASTREAM_TRANSFORMERS: Dict[str, Type[MeshSubjectsTransformer]]
