from _typeshed import Incomplete
from invenio_records_resources.resources.records.args import SearchRequestArgsSchema as SearchRequestArgsSchemaBase

class SearchRequestArgsSchema(SearchRequestArgsSchemaBase):
    allversions: Incomplete
    include_deleted: Incomplete
