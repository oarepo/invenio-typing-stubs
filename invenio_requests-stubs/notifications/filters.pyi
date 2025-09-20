from typing import Any, Dict

class UserRecipientFilter:
    def __init__(self, key: str) -> None: ...
    def __call__(
        self, notification: Any, recipients: Dict[str, Any]
    ) -> Dict[str, Any]: ...
