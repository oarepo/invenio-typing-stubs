from _typeshed import Incomplete

class AuditLogAction:
    context: Incomplete
    id: Incomplete
    resource_type: Incomplete
    message_template: Incomplete
    @classmethod
    def build(cls, identity, resource_id, **kwargs): ...
    def resolve_context(self, data, **kwargs) -> None: ...
    def render_message(self, data): ...
