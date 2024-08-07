"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getrelationsrespwithpagination as shared_getrelationsrespwithpagination
from typing import List, Optional


@dataclasses.dataclass
class GetRelationsV3Request:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Entity id"""
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""Entity Type"""
    exclude_schemas: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'exclude_schemas', 'style': 'form', 'explode': False }})
    r"""Filter results to exclude schemas"""
    from_: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    r"""Starting page number"""
    hydrate: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'hydrate', 'style': 'form', 'explode': True }})
    r"""When true, enables entity hydration to resolve nested $relation & $relation_ref references in-place."""
    include_reverse: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'include_reverse', 'style': 'form', 'explode': True }})
    r"""When true, includes reverse relations in response (other entities pointing to this entity)"""
    include_schemas: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include_schemas', 'style': 'form', 'explode': False }})
    r"""Filter results to only include schemas"""
    size: Optional[int] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    r"""Number of results to return per page"""
    



@dataclasses.dataclass
class GetRelationsV3Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_relations_resp_with_pagination: Optional[shared_getrelationsrespwithpagination.GetRelationsRespWithPagination] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

