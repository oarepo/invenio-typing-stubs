from typing import Type

from invenio_pidstore.providers.base import BaseProvider

class VocabularyIdProvider(BaseProvider): ...

class CustomVocabularyPIDProvider(BaseProvider):
    pid_type: str

class PIDProviderFactory:
    @staticmethod
    def create(pid_type: str, base_cls=...) -> Type[CustomVocabularyPIDProvider]: ...
