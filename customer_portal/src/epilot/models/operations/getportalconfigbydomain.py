"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresp as shared_errorresp
from ..shared import portalconfig as shared_portalconfig
from typing import Optional



@dataclasses.dataclass
class GetPortalConfigByDomainRequest:
    domain: str = dataclasses.field(metadata={'query_param': { 'field_name': 'domain', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class GetPortalConfigByDomainResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    portal_config: Optional[shared_portalconfig.PortalConfig] = dataclasses.field(default=None)
    r"""Portal config retrieved successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

