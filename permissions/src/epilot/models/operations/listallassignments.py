"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import assignment as shared_assignment
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListAllAssignments200ApplicationJSON:
    r"""ok"""
    
    assignments: Optional[list[shared_assignment.Assignment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignments'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class ListAllAssignmentsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_all_assignments_200_application_json_object: Optional[ListAllAssignments200ApplicationJSON] = dataclasses.field(default=None)
    r"""ok"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    