"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class UpdateContactSecurity:
    
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})  
    

@dataclasses.dataclass
class UpdateContactResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    entity_item: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""The returned contact"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    