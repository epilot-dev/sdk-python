"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BatchGetAssignableRequestBody:
    
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    r"""start results from an offset for pagination"""  
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""search query to filter results"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BatchGetAssignable200ApplicationJSON:
    r"""List of assignable results"""
    
    hits: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hits'), 'exclude': lambda f: f is None }})
    r"""total number of search results"""  
    results: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class BatchGetAssignableResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    batch_get_assignable_200_application_json_object: Optional[BatchGetAssignable200ApplicationJSON] = dataclasses.field(default=None)
    r"""List of assignable results"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    