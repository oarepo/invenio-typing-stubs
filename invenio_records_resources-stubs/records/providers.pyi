from _typeshed import Incomplete
from invenio_records_resources.records.api import Record

class ModelPIDProvider:
    @classmethod
    def create(
        cls,
        pid_value: Incomplete,
        record: Record,
        model_field_name: str,
        **kwargs: Incomplete,
    ) -> None: ...
