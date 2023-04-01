"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAllOpportunities200ApplicationJSON:
    r"""The returned opportunities"""
    
    data: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class GetAllOpportunitiesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    get_all_opportunities_200_application_json_object: Optional[GetAllOpportunities200ApplicationJSON] = dataclasses.field(default=None)
    r"""The returned opportunities"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    