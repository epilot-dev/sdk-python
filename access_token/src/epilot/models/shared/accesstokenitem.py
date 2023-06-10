"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import accesstokentype as shared_accesstokentype
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from epilot import utils
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AccessTokenItem:
    r"""The revoked generated Access Token"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human readable name for access token"""
    assignments: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignments'), 'exclude': lambda f: f is None }})
    r"""List of role ids attached to an user"""
    journey_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journey_id'), 'exclude': lambda f: f is None }})
    r"""Journey ID for access token type \\"journey\\" """
    token_type: Optional[shared_accesstokentype.AccessTokenType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_type'), 'exclude': lambda f: f is None }})
    r"""Access token type"""
    

