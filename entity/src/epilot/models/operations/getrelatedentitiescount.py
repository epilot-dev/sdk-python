"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import getrelatedentitiescount as components_getrelatedentitiescount
from typing import List, Optional


@dataclasses.dataclass
class GetRelatedEntitiesCountRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Entity id"""
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""Entity Type"""
    exclude_schemas: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'exclude_schemas', 'style': 'form', 'explode': False }})
    r"""Filter results to exclude schemas"""
    



@dataclasses.dataclass
class GetRelatedEntitiesCountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_related_entities_count: Optional[components_getrelatedentitiescount.GetRelatedEntitiesCount] = dataclasses.field(default=None)
    r"""Success"""
    

