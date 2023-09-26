"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accesstokenitem as shared_accesstokenitem
from typing import Optional



@dataclasses.dataclass
class RevokeAccessTokenRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class RevokeAccessTokenResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    access_token_item: Optional[shared_accesstokenitem.AccessTokenItem] = dataclasses.field(default=None)
    r"""The revoked generated Access Token"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

