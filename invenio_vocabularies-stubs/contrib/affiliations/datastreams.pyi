from typing import Any, Dict

from invenio_vocabularies.contrib.affiliations.config import (
    affiliation_edmo_country_mappings as affiliation_edmo_country_mappings,
)
from invenio_vocabularies.contrib.common.ror.datastreams import (
    RORTransformer as RORTransformer,
)
from invenio_vocabularies.datastreams import StreamEntry as StreamEntry
from invenio_vocabularies.datastreams.errors import TransformerError as TransformerError
from invenio_vocabularies.datastreams.transformers import (
    BaseTransformer as BaseTransformer,
)
from invenio_vocabularies.datastreams.writers import ServiceWriter as ServiceWriter

class AffiliationsServiceWriter(ServiceWriter):
    def __init__(self, *args, **kwargs) -> None: ...

class AffiliationsRORTransformer(RORTransformer):
    def __init__(
        self, *args, vocab_schemes=None, funder_fundref_doi_prefix=None, **kwargs
    ) -> None: ...

class OpenAIREOrganizationTransformer(BaseTransformer):
    def apply(self, stream_entry, **kwargs): ...

class OpenAIREAffiliationsServiceWriter(ServiceWriter):
    def __init__(self, *args, **kwargs) -> None: ...

class EDMOOrganizationTransformer(BaseTransformer):
    def apply(self, stream_entry, **kwargs): ...

VOCABULARIES_DATASTREAM_READERS: Dict[str, type]
VOCABULARIES_DATASTREAM_WRITERS: Dict[str, type]
VOCABULARIES_DATASTREAM_TRANSFORMERS: Dict[str, type]
DATASTREAM_CONFIG: Dict[str, Any]
DATASTREAM_CONFIG_OPENAIRE: Dict[str, Any]
DATASTREAM_CONFIG_EDMO: Dict[str, Any]
