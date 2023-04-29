"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import user as shared_user
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class ListUsersRequest:
    
    limit: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Limit the results size"""
    offset: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Specify the page"""
    org_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'org_ids', 'style': 'form', 'explode': False }})
    r"""Comma-separated list of organization ids to filter by"""
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Query text to filter by"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListUsers200ApplicationJSON:
    r"""List of users"""
    
    users: Optional[list[shared_user.User]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('users'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListUsersResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_users_200_application_json_object: Optional[ListUsers200ApplicationJSON] = dataclasses.field(default=None)
    r"""List of users"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    