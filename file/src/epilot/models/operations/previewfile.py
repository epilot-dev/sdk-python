"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class PreviewFileRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})  
    h: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'h', 'style': 'form', 'explode': True }})
    r"""height"""  
    version: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'version', 'style': 'form', 'explode': True }})
    r"""index of file version"""  
    w: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'w', 'style': 'form', 'explode': True }})
    r"""width"""  
    

@dataclasses.dataclass
class PreviewFileResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    