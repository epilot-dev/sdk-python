"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import entitysearchparams as components_entitysearchparams
from typing import Optional


@dataclasses.dataclass
class ExportEntitiesRequest:
    entity_search_params: Optional[components_entitysearchparams.EntitySearchParams] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    is_template: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'is_template', 'style': 'form', 'explode': True }})
    r"""Pass 'true' to generate import template"""
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'job_id', 'style': 'form', 'explode': True }})
    r"""Export Job Id to get the result"""
    language: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'language', 'style': 'form', 'explode': True }})
    r"""Export headers translation language"""
    



@dataclasses.dataclass
class ExportEntitiesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    

