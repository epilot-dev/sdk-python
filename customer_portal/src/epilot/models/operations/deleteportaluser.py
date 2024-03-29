"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class DeletePortalUserSecurity:
    
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})  
    

@dataclasses.dataclass
class DeletePortalUserResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    delete_portal_user_200_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""The returned portal user id"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    