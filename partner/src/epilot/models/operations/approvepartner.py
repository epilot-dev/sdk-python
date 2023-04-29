"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import partner as shared_partner
from typing import Optional


@dataclasses.dataclass
class ApprovePartnerRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The Id of partner"""
    

@dataclasses.dataclass
class ApprovePartnerResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    partner: Optional[shared_partner.Partner] = dataclasses.field(default=None)
    r"""Approve successfully"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    