from invenio_records_resources.services.records.components.base import (
    ServiceComponent as ServiceComponent,
)

class DataComponent(ServiceComponent):
    def create(
        self, identity, data=None, record=None, errors=None, **kwargs
    ) -> None: ...
    def update(self, identity, data=None, record=None, **kwargs) -> None: ...
