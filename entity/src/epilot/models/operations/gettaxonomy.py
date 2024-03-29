"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import taxonomy as shared_taxonomy
from typing import Optional


@dataclasses.dataclass
class GetTaxonomyRequest:
    
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    r"""Taxonomy slug to return taxonomy for"""  
    

@dataclasses.dataclass
class GetTaxonomyResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    taxonomy: Optional[shared_taxonomy.Taxonomy] = dataclasses.field(default=None)
    r"""Taxonomy"""  
    