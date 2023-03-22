"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import taxonomyclassification as shared_taxonomyclassification
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxonomiesClassificationsSearchRequestBody:
    
    classification_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('classificationIds'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class TaxonomiesClassificationsSearchRequest:
    
    taxonomy_slug: str = dataclasses.field(metadata={'query_param': { 'field_name': 'taxonomySlug', 'style': 'form', 'explode': True }})
    r"""Taxonomy slug"""  
    request_body: Optional[TaxonomiesClassificationsSearchRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxonomiesClassificationsSearch200ApplicationJSON:
    r"""Returns list of taxonomy classifications"""
    
    results: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class TaxonomiesClassificationsSearchResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    taxonomies_classifications_search_200_application_json_object: Optional[TaxonomiesClassificationsSearch200ApplicationJSON] = dataclasses.field(default=None)
    r"""Returns list of taxonomy classifications"""  
    