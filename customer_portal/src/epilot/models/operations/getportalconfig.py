"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import origin as shared_origin
from ..shared import portalconfig as shared_portalconfig
from typing import Optional


@dataclasses.dataclass
class GetPortalConfigSecurity:
    
    epilot_auth: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    portal_auth: Optional[str] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetPortalConfigRequest:
    
    origin: Optional[shared_origin.Origin] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""
    

@dataclasses.dataclass
class GetPortalConfigResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    portal_config: Optional[shared_portalconfig.PortalConfig] = dataclasses.field(default=None)
    r"""ok"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    