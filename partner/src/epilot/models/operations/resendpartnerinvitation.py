"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import partner as shared_partner
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class ResendPartnerInvitationRequestBodyLanguageEnum(str, Enum):
    r"""Language for partner invitation email"""
    EN = 'en'
    DE = 'de'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ResendPartnerInvitationRequestBody:
    
    language: Optional[ResendPartnerInvitationRequestBodyLanguageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})
    r"""Language for partner invitation email"""
    

@dataclasses.dataclass
class ResendPartnerInvitationRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The Id of partner"""
    request_body: Optional[ResendPartnerInvitationRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ResendPartnerInvitationResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    partner: Optional[shared_partner.Partner] = dataclasses.field(default=None)
    r"""Partner Invitation sent successfully"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    