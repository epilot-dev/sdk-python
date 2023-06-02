"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetContractSecurity:
    
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetContractRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of the contract"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetContract200ApplicationJSON:
    r"""The requested contract returned successfully."""
    
    entity: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity'), 'exclude': lambda f: f is None }})
    r"""The contract entity"""
    files: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files'), 'exclude': lambda f: f is None }})
    r"""The related files of the requested contract"""
    orders: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orders'), 'exclude': lambda f: f is None }})
    r"""The related orders of the requested contract"""
    relations: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relations'), 'exclude': lambda f: f is None }})
    r"""The related entities of the requested contract"""
    workflow: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetContractResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    get_contract_200_application_json_object: Optional[GetContract200ApplicationJSON] = dataclasses.field(default=None)
    r"""The requested contract returned successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    