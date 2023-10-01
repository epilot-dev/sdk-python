"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import orgrole as shared_orgrole
from ..shared import partnerrole as shared_partnerrole
from ..shared import rolepayload_1 as shared_rolepayload_1
from ..shared import rolepayload_2 as shared_rolepayload_2
from ..shared import rolepayload_3 as shared_rolepayload_3
from ..shared import rolepayload_4 as shared_rolepayload_4
from ..shared import sharerole as shared_sharerole
from ..shared import userrole as shared_userrole
from typing import Optional, Union



@dataclasses.dataclass
class PutRoleRequest:
    role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'roleId', 'style': 'simple', 'explode': False }})
    role_payload: Optional[Union[shared_rolepayload_1.RolePayload1, shared_rolepayload_2.RolePayload2, shared_rolepayload_3.RolePayload3, shared_rolepayload_4.RolePayload4]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PutRoleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    role: Optional[Union[shared_userrole.UserRole, shared_orgrole.OrgRole, shared_sharerole.ShareRole, shared_partnerrole.PartnerRole]] = dataclasses.field(default=None)
    r"""ok"""
    

