from typing import List

from invenio_vocabularies.services.facets import VocabularyLabels as VocabularyLabels
from invenio_vocabularies.services.facets import lazy_get_label as lazy_get_label

class AffiliationsLabels(VocabularyLabels):
    fields: List[str]
    def __init__(
        self, vocabulary, cache: bool = True, cache_ttl: int = 3600, service_id=None
    ) -> None: ...
