"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any, Optional

class SearchAssignableRequestBodyTypesEnum(str, Enum):
    USER = "user"
    PARTNER_USER = "partner_user"
    PARTNER_ORGANIZATION = "partner_organization"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchAssignableRequestBody:
    
    q: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('q') }})
    r"""search query to filter results"""  
    from_: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from'), 'exclude': lambda f: f is None }})
    r"""start results from an offset for pagination"""  
    org_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_ids'), 'exclude': lambda f: f is None }})
    r"""filter results to specific organizations. defaults to all orgs"""  
    size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size'), 'exclude': lambda f: f is None }})
    r"""limit number of results to return"""  
    types: Optional[list[SearchAssignableRequestBodyTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('types'), 'exclude': lambda f: f is None }})
    r"""filter results to specific types of assignables. defaults to all types"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchAssignable200ApplicationJSON:
    r"""List of assignable results"""
    
    hits: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hits'), 'exclude': lambda f: f is None }})
    r"""total number of search results"""  
    results: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class SearchAssignableResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    search_assignable_200_application_json_object: Optional[SearchAssignable200ApplicationJSON] = dataclasses.field(default=None)
    r"""List of assignable results"""  
    