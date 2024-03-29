"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListCurrentRoles200ApplicationJSON:
    r"""ok"""
    
    roles: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('roles'), 'exclude': lambda f: f is None }})  
    

@dataclasses.dataclass
class ListCurrentRolesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    list_current_roles_200_application_json_object: Optional[ListCurrentRoles200ApplicationJSON] = dataclasses.field(default=None)
    r"""ok"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    