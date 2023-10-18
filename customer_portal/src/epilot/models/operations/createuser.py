"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createuserrequest as shared_createuserrequest
from ..shared import errorresp as shared_errorresp
from ..shared import origin as shared_origin
from ..shared import portaluser as shared_portaluser
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class CreateUserRequest:
    create_user_request: shared_createuserrequest.CreateUserRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Portal user payload"""
    origin: shared_origin.Origin = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""
    


class CreateUser201ApplicationJSONMessage(str, Enum):
    USER_CREATED_SUCCESSFULLY = 'User created successfully'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateUser201ApplicationJSON:
    r"""User created successfully."""
    message: CreateUser201ApplicationJSONMessage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    response: shared_portaluser.PortalUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response') }})
    r"""The portal user entity"""
    



@dataclasses.dataclass
class CreateUserResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_user_201_application_json_object: Optional[CreateUser201ApplicationJSON] = dataclasses.field(default=None)
    r"""User created successfully."""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""The request could not be validated"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

