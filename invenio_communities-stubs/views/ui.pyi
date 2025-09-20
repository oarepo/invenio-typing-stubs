from flask.app import Flask
from flask.blueprints import Blueprint
from invenio_communities.communities.resources.serializer import (
    UICommunityJSONSerializer as UICommunityJSONSerializer,
)
from invenio_communities.proxies import current_communities as current_communities

from ..errors import CommunityDeletedError as CommunityDeletedError
from ..errors import LogoNotFoundError as LogoNotFoundError
from ..searchapp import search_app_context as search_app_context
from .communities import communities_about as communities_about
from .communities import communities_curation_policy as communities_curation_policy
from .communities import communities_frontpage as communities_frontpage
from .communities import communities_new as communities_new
from .communities import communities_new_subcommunity as communities_new_subcommunity
from .communities import communities_requests as communities_requests
from .communities import communities_search as communities_search
from .communities import communities_settings as communities_settings
from .communities import communities_settings_pages as communities_settings_pages
from .communities import (
    communities_settings_privileges as communities_settings_privileges,
)
from .communities import (
    communities_settings_submission_policy as communities_settings_submission_policy,
)
from .communities import communities_subcommunities as communities_subcommunities
from .communities import community_theme_css_config as community_theme_css_config
from .communities import invitations as invitations
from .communities import members as members
from .decorators import warn_deprecation as warn_deprecation

def not_found_error(error): ...
def record_tombstone_error(error): ...
def record_permission_denied_error(error): ...
def create_ui_blueprint(app: Flask) -> Blueprint: ...
