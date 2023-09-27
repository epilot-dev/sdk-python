"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import orgrole as shared_orgrole
from ..shared import partnerrole as shared_partnerrole
from ..shared import sharerole as shared_sharerole
from ..shared import userrole as shared_userrole
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchRoles200ApplicationJSON:
    r"""ok"""
    hits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hits'), 'exclude': lambda f: f is None }})
    results: Optional[list[Union[shared_userrole.UserRole, shared_orgrole.OrgRole, shared_sharerole.ShareRole, shared_partnerrole.PartnerRole]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class SearchRolesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    search_roles_200_application_json_object: Optional[SearchRoles200ApplicationJSON] = dataclasses.field(default=None)
    r"""ok"""
    

