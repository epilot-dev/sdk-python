"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DollarCreateOpportunityRequest:
    
    request_body: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})  
    x_ivy_org_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Ivy-Org-ID', 'style': 'simple', 'explode': False }})
    r"""The target Organization Id represented by the caller"""  
    

@dataclasses.dataclass
class DollarCreateOpportunityResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error: Optional[Any] = dataclasses.field(default=None)
    r"""Invalid payload"""  
    opportunity: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""The new Opportunity."""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    