"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityschema as shared_entityschema
from ..shared import entityschemaitem as shared_entityschemaitem
from typing import Optional


@dataclasses.dataclass
class PutSchemaRequest:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""Entity Type"""
    draft: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'draft', 'style': 'form', 'explode': True }})
    entity_schema: Optional[shared_entityschema.EntitySchema] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PutSchemaResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    entity_schema_item: Optional[shared_entityschemaitem.EntitySchemaItem] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

