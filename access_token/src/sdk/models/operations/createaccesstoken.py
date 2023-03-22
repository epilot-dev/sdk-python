"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import accesstokentype_enum as shared_accesstokentype_enum
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAccessToken201ApplicationJSON:
    r"""The new generated Access Token"""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human readable name for access token"""  
    assignments: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignments'), 'exclude': lambda f: f is None }})
    r"""List of role ids attached to an user"""  
    journey_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journey_id'), 'exclude': lambda f: f is None }})
    r"""Journey ID for access token type \"journey\""""  
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""A JWT Access Token"""  
    token_type: Optional[shared_accesstokentype_enum.AccessTokenTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_type'), 'exclude': lambda f: f is None }})
    r"""Access token type"""  
    

@dataclasses.dataclass
class CreateAccessTokenResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_access_token_201_application_json_object: Optional[CreateAccessToken201ApplicationJSON] = dataclasses.field(default=None)
    r"""The new generated Access Token"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    