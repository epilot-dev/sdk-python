"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class UpdateEntityRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})

    r"""Entity id"""
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})

    r"""Entity Type"""
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'activity_id', 'style': 'form', 'explode': True }})

    r"""Activity to include in event feed"""
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})

    r"""Don't wait for updated entity to become available in Search API. Useful for large migrations"""
    request_body: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})

    

@dataclasses.dataclass
class UpdateEntityResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    entity_item: Optional[dict[str, Any]] = dataclasses.field(default=None)

    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    