"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import origin as shared_origin
from ..shared import portalconfig as shared_portalconfig
from typing import Optional


@dataclasses.dataclass
class GetPublicPortalConfigRequest:
    
    org_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'org_id', 'style': 'form', 'explode': True }})
    origin: shared_origin.Origin = dataclasses.field(metadata={'query_param': { 'field_name': 'origin', 'style': 'form', 'explode': True }})
    r"""Origin of the portal"""
    

@dataclasses.dataclass
class GetPublicPortalConfigResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    portal_config: Optional[shared_portalconfig.PortalConfig] = dataclasses.field(default=None)
    r"""Portal config retrieved successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    