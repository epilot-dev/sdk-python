"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createssouserrequest as shared_createssouserrequest
from ..shared import errorresp as shared_errorresp
from ..shared import origin as shared_origin
from ..shared import portaluser as shared_portaluser
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class CreateSSOUserSecurity:
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class CreateSSOUserRequest:
    create_sso_user_request: shared_createssouserrequest.CreateSSOUserRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Portal user payload"""
    origin: shared_origin.Origin = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSSOUser201ApplicationJSON:
    r"""SSO User created successfully."""
    data: Optional[shared_portaluser.PortalUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""The portal user entity"""
    



@dataclasses.dataclass
class CreateSSOUserResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_sso_user_201_application_json_object: Optional[CreateSSOUser201ApplicationJSON] = dataclasses.field(default=None)
    r"""SSO User created successfully."""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""The request could not be validated"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

