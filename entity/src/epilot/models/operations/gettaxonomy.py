"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import taxonomy as components_taxonomy
from typing import Optional


@dataclasses.dataclass
class GetTaxonomyRequest:
    taxonomy_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'taxonomySlug', 'style': 'simple', 'explode': False }})
    r"""Taxonomy slug"""
    



@dataclasses.dataclass
class GetTaxonomyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    taxonomy: Optional[components_taxonomy.Taxonomy] = dataclasses.field(default=None)
    r"""Taxonomy"""
    

