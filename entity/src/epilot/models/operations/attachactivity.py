"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import activityitem as shared_activityitem
from typing import Optional


@dataclasses.dataclass
class AttachActivityRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Activity Id"""  
    entities: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entities', 'style': 'form', 'explode': False }})
    r"""Comma-separated list of entities which the activity primarily concerns"""  
    

@dataclasses.dataclass
class AttachActivityResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    activity_item: Optional[shared_activityitem.ActivityItem] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    