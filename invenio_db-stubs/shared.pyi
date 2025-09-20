from typing import Any

from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy  # type: ignore[import-untyped]
from sqlalchemy import MetaData  # type: ignore[import-untyped]

NAMING_CONVENTION: dict[str, str]
metadata: MetaData

class SQLAlchemy(FlaskSQLAlchemy):
    model: Any

    def apply_driver_hacks(self, app: Any, sa_url: Any, options: Any) -> None: ...

def do_sqlite_connect(dbapi_connection: Any, connection_record: Any) -> None: ...
def do_sqlite_begin(dbapi_connection: Any) -> None: ...

db: Any
