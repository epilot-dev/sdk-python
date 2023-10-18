"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import userv2 as shared_userv2
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional


@dataclasses.dataclass
class ListUsersV2Request:
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Limit the results size"""
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Specify the page"""
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Query text to filter by"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListUsersV2200ApplicationJSON:
    r"""List of organization users"""
    results: Optional[List[shared_userv2.UserV2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class ListUsersV2Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    list_users_v2_200_application_json_object: Optional[ListUsersV2200ApplicationJSON] = dataclasses.field(default=None)
    r"""List of organization users"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

