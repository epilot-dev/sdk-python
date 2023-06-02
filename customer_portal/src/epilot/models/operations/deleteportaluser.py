"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class DeletePortalUserSecurity:
    
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    
class DeletePortalUser200ApplicationJSONMessage(str, Enum):
    USER_SUCCESFULLY_DELETED = 'User Succesfully Deleted'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeletePortalUser200ApplicationJSON:
    r"""Portal user deleted successfully."""
    
    data: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""Entity ID"""
    message: Optional[DeletePortalUser200ApplicationJSONMessage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class DeletePortalUserResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_portal_user_200_application_json_object: Optional[DeletePortalUser200ApplicationJSON] = dataclasses.field(default=None)
    r"""Portal user deleted successfully."""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    