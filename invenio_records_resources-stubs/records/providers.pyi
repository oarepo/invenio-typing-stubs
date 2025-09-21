from typing import Any

class ModelPIDProvider:
    @classmethod
    def create(
        cls, pid_value: str, record: Any, model_field_name: str, **kwargs: Any
    ) -> None: ...
