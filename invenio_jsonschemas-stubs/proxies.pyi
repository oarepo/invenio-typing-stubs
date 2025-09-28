from __future__ import annotations

from jsonref import JsonRef
from werkzeug.local import LocalProxy

from .ext import InvenioJSONSchemasState, JSONSchema

current_jsonschemas: LocalProxy[InvenioJSONSchemasState]
current_refresolver_store: LocalProxy[dict[str, JSONSchema | JsonRef]]
