from typing import Any, Dict, Type

from invenio_vocabularies.contrib.subjects.config import nvs_file_url as nvs_file_url
from invenio_vocabularies.datastreams.errors import TransformerError as TransformerError
from invenio_vocabularies.datastreams.readers import RDFReader as RDFReader
from invenio_vocabularies.datastreams.transformers import (
    RDFTransformer as RDFTransformer,
)

class NVSSubjectsTransformer(RDFTransformer): ...

VOCABULARIES_DATASTREAM_TRANSFORMERS: Dict[str, Type[NVSSubjectsTransformer]]
DATASTREAM_CONFIG: Dict[str, Any]
