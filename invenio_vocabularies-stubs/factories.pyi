from typing import Any

from invenio_vocabularies.contrib.affiliations.datastreams import (
    DATASTREAM_CONFIG as affiliations_ds_config,
)
from invenio_vocabularies.contrib.affiliations.datastreams import (
    DATASTREAM_CONFIG_EDMO as affiliations_edmo_ds_config,
)
from invenio_vocabularies.contrib.affiliations.datastreams import (
    DATASTREAM_CONFIG_OPENAIRE as affiliations_openaire_ds_config,
)
from invenio_vocabularies.contrib.awards.datastreams import (
    DATASTREAM_CONFIG as awards_ds_config,
)
from invenio_vocabularies.contrib.awards.datastreams import (
    DATASTREAM_CONFIG_CORDIS as awards_cordis_ds_config,
)
from invenio_vocabularies.contrib.funders.datastreams import (
    DATASTREAM_CONFIG as funders_ds_config,
)
from invenio_vocabularies.contrib.names.datastreams import (
    DATASTREAM_CONFIG as names_ds_config,
)
from invenio_vocabularies.contrib.subjects.datastreams import (
    DATASTREAM_CONFIG as subjects_ds_config,
)
from invenio_vocabularies.contrib.subjects.euroscivoc.datastreams import (
    DATASTREAM_CONFIG as euroscivoc_ds_config,
)
from invenio_vocabularies.contrib.subjects.gemet.datastreams import (
    DATASTREAM_CONFIG as gemet_ds_config,
)
from invenio_vocabularies.contrib.subjects.nvs.datastreams import (
    DATASTREAM_CONFIG as nvs_ds_config,
)

class VocabularyConfig:
    config: Any
    vocabulary_name: Any
    def get_config(self, filepath=None, origin=None): ...
    def get_service(self): ...

class NamesVocabularyConfig(VocabularyConfig):
    config = names_ds_config
    vocabulary_name: str

class FundersVocabularyConfig(VocabularyConfig):
    config = funders_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class SubjectsVocabularyConfig(VocabularyConfig):
    config = subjects_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class AwardsVocabularyConfig(VocabularyConfig):
    config = awards_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class AwardsCordisVocabularyConfig(VocabularyConfig):
    config = awards_cordis_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class AffiliationsVocabularyConfig(VocabularyConfig):
    config = affiliations_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class AffiliationsOpenAIREVocabularyConfig(VocabularyConfig):
    config = affiliations_openaire_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class AffiliationsEDMOVocabularyConfig(VocabularyConfig):
    config = affiliations_edmo_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class SubjectsEuroSciVocVocabularyConfig(VocabularyConfig):
    config = euroscivoc_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class SubjectsGEMETVocabularyConfig(VocabularyConfig):
    config = gemet_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

class SubjectsNVSVocabularyConfig(VocabularyConfig):
    config = nvs_ds_config
    vocabulary_name: str
    def get_service(self) -> None: ...

def get_vocabulary_config(vocabulary): ...
