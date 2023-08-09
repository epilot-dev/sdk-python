"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accesstokenitem as shared_accesstokenitem
from ..shared import accesstokentype as shared_accesstokentype
from typing import Optional



@dataclasses.dataclass
class ListAccessTokensRequest:
    token_type: Optional[list[shared_accesstokentype.AccessTokenType]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'token_type', 'style': 'form', 'explode': True }})
    r"""Filter by token types"""
    




@dataclasses.dataclass
class ListAccessTokensResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    access_token_items: Optional[list[shared_accesstokenitem.AccessTokenItem]] = dataclasses.field(default=None)
    r"""List of Access Tokens"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

