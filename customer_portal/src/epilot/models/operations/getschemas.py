"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional



@dataclasses.dataclass
class GetSchemasSecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetSchemas200ApplicationJSON:
    r"""Retrieved schemas for an organization successfully."""
    schemas: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetSchemasResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    get_schemas_200_application_json_object: Optional[GetSchemas200ApplicationJSON] = dataclasses.field(default=None)
    r"""Retrieved schemas for an organization successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

