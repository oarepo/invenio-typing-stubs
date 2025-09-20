from typing import Any

from invenio_vocabularies.contrib.affiliations.api import Affiliation as Affiliation
from invenio_vocabularies.contrib.names.config import (
    NamesSearchOptions as NamesSearchOptions,
)
from invenio_vocabularies.contrib.names.config import (
    service_components as service_components,
)
from invenio_vocabularies.contrib.names.permissions import (
    NamesPermissionPolicy as NamesPermissionPolicy,
)
from invenio_vocabularies.contrib.names.schema import NameSchema as NameSchema

name_relations: Any
record_type: Any
