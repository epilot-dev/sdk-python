"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetTokenV2200ApplicationJSON:
    r"""JWT Token"""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""JWT Token"""
    




@dataclasses.dataclass
class GetTokenV2Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_token_v2_200_application_json_object: Optional[GetTokenV2200ApplicationJSON] = dataclasses.field(default=None)
    r"""JWT Token"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

