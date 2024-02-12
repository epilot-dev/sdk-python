"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import entityschema as components_entityschema
from ...models.components import entityschemaitem as components_entityschemaitem
from typing import Optional


@dataclasses.dataclass
class PutSchemaRequest:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""Entity Type"""
    entity_schema: Optional[components_entityschema.EntitySchema] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    draft: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'draft', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class PutSchemaResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    entity_schema_item: Optional[components_entityschemaitem.EntitySchemaItem] = dataclasses.field(default=None)
    r"""Success"""
    

