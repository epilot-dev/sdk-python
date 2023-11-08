"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import schema as components_schema
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional


@dataclasses.dataclass
class GetSchemasSecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSchemasResponseBody:
    r"""Retrieved schemas for an organization successfully."""
    schemas: Optional[List[components_schema.Schema]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class GetSchemasResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[GetSchemasResponseBody] = dataclasses.field(default=None)
    r"""Retrieved schemas for an organization successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

