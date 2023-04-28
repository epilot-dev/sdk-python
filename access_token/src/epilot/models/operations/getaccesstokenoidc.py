"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccessTokenOIDC200ApplicationJSON:
    r"""OpenID Configuration"""
    
    issuer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issuer'), 'exclude': lambda f: f is None }})

    jwks_uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jwks_uri'), 'exclude': lambda f: f is None }})

    

@dataclasses.dataclass
class GetAccessTokenOIDCResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    get_access_token_oidc_200_application_json_object: Optional[GetAccessTokenOIDC200ApplicationJSON] = dataclasses.field(default=None)

    r"""OpenID Configuration"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    