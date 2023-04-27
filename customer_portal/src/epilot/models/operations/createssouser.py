"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import origin_enum as shared_origin_enum
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclasses.dataclass
class CreateSSOUserSecurity:
    
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSSOUserRequestBody:
    r"""Portal payload"""
    
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})  
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name'), 'exclude': lambda f: f is None }})  
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class CreateSSOUserRequest:
    
    origin: shared_origin_enum.OriginEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""  
    request_body: CreateSSOUserRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Portal payload"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSSOUser201ApplicationJSON:
    r"""Success - SSO User created with success."""
    
    data: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class CreateSSOUserResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_sso_user_201_application_json_object: Optional[CreateSSOUser201ApplicationJSON] = dataclasses.field(default=None)
    r"""Success - SSO User created with success."""  
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Validation Errors"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    