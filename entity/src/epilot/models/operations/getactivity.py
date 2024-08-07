"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import activityitem as shared_activityitem
from typing import Optional


@dataclasses.dataclass
class GetActivityRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Activity Id"""
    operations_from: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'operations_from', 'style': 'form', 'explode': True }})
    r"""Pagination offset for operations"""
    operations_size: Optional[int] = dataclasses.field(default=25, metadata={'query_param': { 'field_name': 'operations_size', 'style': 'form', 'explode': True }})
    r"""Maximum number of operations to include in response (default: 10)"""
    



@dataclasses.dataclass
class GetActivityResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    activity_item: Optional[shared_activityitem.ActivityItem] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

