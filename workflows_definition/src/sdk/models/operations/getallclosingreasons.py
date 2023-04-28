"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import closingreasons as shared_closingreasons
from typing import Optional


@dataclasses.dataclass
class GetAllClosingReasonsRequest:
    
    include_inactive: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeInactive', 'style': 'form', 'explode': True }})

    r"""Filter Closing Reasons by status like active inactiv"""
    

@dataclasses.dataclass
class GetAllClosingReasonsResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    closing_reasons: Optional[shared_closingreasons.ClosingReasons] = dataclasses.field(default=None)

    r"""Returns the entire catalog of closing reasons per organization"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    