from typing import Dict


class BooleanCF:
    def __init__(self, name: str, **kwargs): ...
    @property
    def mapping(self) -> Dict[str, str]: ...
