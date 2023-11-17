"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import getexecutionsresp as components_getexecutionsresp
from typing import Optional


@dataclasses.dataclass
class GetExecutionsRequest:
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entity_id', 'style': 'form', 'explode': True }})
    from_: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    r"""Pagination: starting for results"""
    size: Optional[int] = dataclasses.field(default=25, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    r"""Pagination: max number of results to return"""
    



@dataclasses.dataclass
class GetExecutionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_executions_resp: Optional[components_getexecutionsresp.GetExecutionsResp] = dataclasses.field(default=None)
    r"""List of automation executions"""
    

