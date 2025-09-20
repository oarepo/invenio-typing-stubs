from flask.cli import with_appcontext
from invenio_vocabularies.datastreams import DataStreamFactory as DataStreamFactory
from invenio_vocabularies.factories import (
    get_vocabulary_config as get_vocabulary_config,
)

def vocabularies() -> None: ...
@with_appcontext
def import_vocab(vocabulary, filepath=None, origin=None, num_samples=None) -> None: ...
@with_appcontext
def update(vocabulary, filepath=None, origin=None) -> None: ...
@with_appcontext
def convert(
    vocabulary, filepath=None, origin=None, target=None, num_samples=None
) -> None: ...
@with_appcontext
def delete(vocabulary, identifier, all) -> None: ...
