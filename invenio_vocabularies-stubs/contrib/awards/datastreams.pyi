from collections.abc import Generator
from typing import Any

from invenio_vocabularies.contrib.awards.config import (
    awards_ec_ror_id as awards_ec_ror_id,
)
from invenio_vocabularies.contrib.awards.config import (
    awards_openaire_funders_mapping as awards_openaire_funders_mapping,
)
from invenio_vocabularies.datastreams.errors import ReaderError as ReaderError
from invenio_vocabularies.datastreams.errors import TransformerError as TransformerError
from invenio_vocabularies.datastreams.readers import BaseReader as BaseReader
from invenio_vocabularies.datastreams.transformers import (
    BaseTransformer as BaseTransformer,
)
from invenio_vocabularies.datastreams.writers import ServiceWriter as ServiceWriter

class AwardsServiceWriter(ServiceWriter):
    def __init__(self, *args, **kwargs) -> None: ...

class OpenAIREProjectTransformer(BaseTransformer):
    def apply(self, stream_entry, **kwargs): ...

class CORDISProjectHTTPReader(BaseReader):
    def read(self, item=None, *args, **kwargs) -> Generator[Any]: ...

class CORDISProjectTransformer(BaseTransformer):
    def apply(self, stream_entry, **kwargs): ...

class CORDISAwardsServiceWriter(ServiceWriter):
    def __init__(self, *args, **kwargs) -> None: ...

VOCABULARIES_DATASTREAM_READERS: dict[str, type[CORDISProjectHTTPReader]]
VOCABULARIES_DATASTREAM_TRANSFORMERS: dict[
    str, type[OpenAIREProjectTransformer | CORDISProjectTransformer]
]
VOCABULARIES_DATASTREAM_WRITERS: dict[
    str, type[AwardsServiceWriter | CORDISAwardsServiceWriter]
]
DATASTREAM_CONFIG_CORDIS: dict[str, list[dict[str, str | dict[str, str]]]]
DATASTREAM_CONFIG: dict[str, list[dict[str, str | dict[str, str]]]]
