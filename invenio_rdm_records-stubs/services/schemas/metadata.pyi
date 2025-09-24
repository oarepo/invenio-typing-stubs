from __future__ import annotations

from marshmallow import Schema

class PersonOrOrganizationSchema(Schema):
    NAMES: list[str]
    type: Any
    name: Any
    given_name: Any
    family_name: Any
    identifiers: Any
    def validate_names(self, data, **kwargs): ...
    def update_names(self, data, **kwargs): ...

def validate_affiliations_data(data) -> None: ...

class CreatorSchema(Schema):
    person_or_org: Any
    role: Any
    affiliations: Any
    def validate_affiliations(self, data, **kwargs): ...

class ContributorSchema(Schema):
    person_or_org: Any
    role: Any
    affiliations: Any
    def validate_affiliations(self, data, **kwargs): ...

class TitleSchema(Schema):
    title: Any
    type: Any
    lang: Any

class DescriptionSchema(Schema):
    description: Any
    type: Any
    lang: Any

def _is_uri(uri) -> bool: ...

class PropsSchema(Schema):
    url: Any
    scheme: Any

class RightsSchema(Schema):
    id: Any
    title: Any
    description: Any
    icon: Any
    props: Any
    link: Any
    def validate_title(self, value): ...
    def validate_description(self, value): ...
    def validate_rights(self, data, **kwargs): ...

class DateSchema(Schema):
    date: Any
    type: Any
    description: Any

class RelatedIdentifierSchema(Schema):
    relation_type: Any
    resource_type: Any
    def validate_related_identifier(self, data, **kwargs): ...

class FundingSchema(Schema):
    funder: Any
    award: Any

class ReferenceSchema(Schema):
    reference: Any

class PointSchema(Schema):
    lat: Any
    lon: Any

class LocationSchema(Schema):
    geometry: Any
    place: Any
    identifiers: Any
    description: Any
    def validate_data(self, data, **kwargs): ...

class FeatureSchema(Schema):
    features: Any

class MetadataSchema(Schema):
    resource_type: Any
    creators: Any
    title: Any
    additional_titles: Any
    publisher: Any
    publication_date: Any
    subjects: Any
    contributors: Any
    dates: Any
    languages: Any
    identifiers: Any
    related_identifiers: Any
    sizes: Any
    formats: Any
    version: Any
    rights: Any
    copyright: Any
    description: Any
    additional_descriptions: Any
    locations: Any
    funding: Any
    references: Any
