"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import activity as shared_activity
from ..shared import activityitem as shared_activityitem
from ..shared import errorresp as shared_errorresp
from typing import Optional



@dataclasses.dataclass
class CreateCustomEntityActivitySecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class CreateCustomEntityActivityRequest:
    activity: Optional[shared_activity.Activity] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    entities: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entities', 'style': 'form', 'explode': False }})
    r"""Comma-separated list of entities which the activity primarily concerns"""
    




@dataclasses.dataclass
class CreateCustomEntityActivityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    activity_item: Optional[shared_activityitem.ActivityItem] = dataclasses.field(default=None)
    r"""Success"""
    error_resp: Optional[shared_errorresp.ErrorResp] = dataclasses.field(default=None)
    r"""Could not authenticate the user"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

