"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import userv2 as shared_userv2
from typing import Optional


@dataclasses.dataclass
class GetUserV2Request:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The Id of user"""
    

@dataclasses.dataclass
class GetUserV2Response:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    user_v2: Optional[shared_userv2.UserV2] = dataclasses.field(default=None)
    r"""The returned user"""
    