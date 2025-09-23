import click
from flask.cli import with_appcontext
from invenio_communities.fixtures.demo import (
    create_fake_community as create_fake_community,
)
from invenio_communities.fixtures.tasks import (
    create_demo_community as create_demo_community,
)
from invenio_communities.proxies import (
    current_communities as current_communities,
)
from invenio_communities.proxies import (
    current_identities_cache as current_identities_cache,
)

def communities() -> None: ...
def identity_cache() -> None: ...
@with_appcontext
def clear() -> None: ...
@with_appcontext
def demo() -> None: ...
@with_appcontext
def rebuild_index() -> None: ...
def custom_fields() -> None: ...
@with_appcontext
@click.option("-f", "--field-name", type=str, required=False, multiple=True)
def create_communities_custom_field(field_name: tuple[str, ...]) -> None: ...
@with_appcontext
@click.option("-f", "--field-name", type=str, required=True, multiple=False)
def custom_field_exists_in_communities(field_name: str) -> None: ...
