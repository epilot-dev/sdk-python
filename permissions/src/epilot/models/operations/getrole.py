"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import orgrole as shared_orgrole
from ..shared import partnerrole as shared_partnerrole
from ..shared import sharerole as shared_sharerole
from ..shared import userrole as shared_userrole
from typing import Optional, Union


@dataclasses.dataclass
class GetRoleRequest:
    role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'roleId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetRoleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    role: Optional[Union[shared_userrole.UserRole, shared_orgrole.OrgRole, shared_sharerole.ShareRole, shared_partnerrole.PartnerRole]] = dataclasses.field(default=None)
    r"""ok"""
    

