"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import classificationsupdate as shared_classificationsupdate
from ..shared import taxonomyclassification as shared_taxonomyclassification
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional



@dataclasses.dataclass
class UpdateClassificationsForTaxonomyRequest:
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    r"""Taxonomy slug"""
    classifications_update: Optional[shared_classificationsupdate.ClassificationsUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateClassificationsForTaxonomy200ApplicationJSONDeleted:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateClassificationsForTaxonomy200ApplicationJSON:
    r"""Taxonomies classifications"""
    created: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'exclude': lambda f: f is None }})
    deleted: Optional[UpdateClassificationsForTaxonomy200ApplicationJSONDeleted] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted'), 'exclude': lambda f: f is None }})
    updated: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class UpdateClassificationsForTaxonomyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_classifications_for_taxonomy_200_application_json_object: Optional[UpdateClassificationsForTaxonomy200ApplicationJSON] = dataclasses.field(default=None)
    r"""Taxonomies classifications"""
    

