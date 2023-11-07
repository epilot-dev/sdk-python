"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import opportunity as components_opportunity
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, Optional


@dataclasses.dataclass
class UpdateOpportunitySecurity:
    portal_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class UpdateOpportunityRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of opportunity"""
    request_body: Dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Requested opportunity body to update"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateOpportunityResponseBody:
    r"""Updated the opportunity successfully."""
    data: Optional[components_opportunity.Opportunity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""The opportunity entity"""
    



@dataclasses.dataclass
class UpdateOpportunityResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[UpdateOpportunityResponseBody] = dataclasses.field(default=None)
    r"""Updated the opportunity successfully."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

