"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import taxonomy as shared_taxonomy
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListTaxonomies200ApplicationJSON:
    r"""Returns list of taxonomies in an organisation"""
    
    results: Optional[list[shared_taxonomy.Taxonomy]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListTaxonomiesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_taxonomies_200_application_json_object: Optional[ListTaxonomies200ApplicationJSON] = dataclasses.field(default=None)
    r"""Returns list of taxonomies in an organisation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    