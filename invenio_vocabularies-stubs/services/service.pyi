from typing import Any, Dict, List, Optional

from flask_principal import Identity
from invenio_db.uow import UnitOfWork
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.records.results import RecordList
from invenio_vocabularies.records.models import VocabularyType as VocabularyType
from invenio_vocabularies.services.tasks import process_datastream as process_datastream

class VocabularyTypeService(RecordService): ...

class VocabulariesService(RecordService):
    @property
    def task_schema(self): ...
    def create_type(
        self,
        identity: Identity,
        id: str,
        pid_type: str,
        uow: Optional[UnitOfWork] = None,
    ) -> VocabularyType: ...
    def read_all(  # type: ignore[override]
        self,
        identity: Identity,
        fields: List[str],
        type: str,
        cache: bool = True,
        extra_filter: str = "",
        **kwargs,
    ) -> RecordList: ...
    def launch(self, identity: Identity, data: Dict[str, Any]): ...
