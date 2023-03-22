"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class GetJourneyRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Journey ID"""  
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orgId', 'style': 'form', 'explode': True }})
    r"""Organization ID"""  
    source: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'source', 'style': 'form', 'explode': True }})
    r"""What source ID. Journey or Entity ID"""  
    

@dataclasses.dataclass
class GetJourneyResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    journey_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    