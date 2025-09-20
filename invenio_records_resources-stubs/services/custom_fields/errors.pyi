from typing import Set


class CustomFieldsInvalidArgument:
    def __init__(self, arg_name: str): ...


class CustomFieldsNotConfigured:
    def __init__(self, field_names: Set[str]): ...


class InvalidCustomFieldsNamespace:
    def __init__(self, field_name: str, given_namespace: str): ...
