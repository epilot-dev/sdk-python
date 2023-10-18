"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import assignment as shared_assignment
from typing import Optional


@dataclasses.dataclass
class RemoveAssignmentRequest:
    role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'roleId', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class RemoveAssignmentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    assignment: Optional[shared_assignment.Assignment] = dataclasses.field(default=None)
    r"""ok"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

