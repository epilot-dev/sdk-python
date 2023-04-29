"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import grant as shared_grant
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilot import utils
from marshmallow import fields
from typing import Any, Optional

class PutRoleRequestBody4TypeEnum(str, Enum):
    PARTNER_ROLE = 'partner_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutRoleRequestBody4:
    r"""A role that appears in another organization's role list that can be assigned but not modified by the partner organization."""
    
    grants: list[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: PutRoleRequestBody4TypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    partner_org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partner_org_id'), 'exclude': lambda f: f is None }})
    
class PutRoleRequestBody3TypeEnum(str, Enum):
    SHARE_ROLE = 'share_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutRoleRequestBody3:
    r"""A role that can be assigned to users in other organizations for sharing purposes."""
    
    grants: list[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: PutRoleRequestBody3TypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    
class PutRoleRequestBody2TypeEnum(str, Enum):
    ORG_ROLE = 'org_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutRoleRequestBody2:
    r"""A role automatically applied to all users in an organization."""
    
    grants: list[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: PutRoleRequestBody2TypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    
class PutRoleRequestBody1TypeEnum(str, Enum):
    USER_ROLE = 'user_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutRoleRequestBody1:
    r"""A standard user role. Must be explicitly assigned to users."""
    
    grants: list[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: PutRoleRequestBody1TypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    

@dataclasses.dataclass
class PutRoleRequest:
    
    role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'roleId', 'style': 'simple', 'explode': False }})
    request_body: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PutRoleResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    role: Optional[Any] = dataclasses.field(default=None)
    r"""ok"""
    