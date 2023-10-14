"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import origin as shared_origin
from ..shared import portalconfig as shared_portalconfig
from typing import Optional



@dataclasses.dataclass
class GetOrgPortalConfigSecurity:
    epilot_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class GetOrgPortalConfigRequest:
    origin: shared_origin.Origin = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""
    




@dataclasses.dataclass
class GetOrgPortalConfigResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    portal_config: Optional[shared_portalconfig.PortalConfig] = dataclasses.field(default=None)
    r"""Portal config retrieved successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

