"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import grant as shared_grant
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilot import utils
from typing import List, Optional

class RolePayload4Type(str, Enum):
    PARTNER_ROLE = 'partner_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RolePayload4:
    r"""A role that appears in another organization's role list that can be assigned but not modified by the partner organization."""
    grants: List[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: RolePayload4Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    partner_org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partner_org_id'), 'exclude': lambda f: f is None }})
    


class RolePayload3Type(str, Enum):
    SHARE_ROLE = 'share_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RolePayload3:
    r"""A role that can be assigned to users in other organizations for sharing purposes."""
    grants: List[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: RolePayload3Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    


class RolePayload2Type(str, Enum):
    ORG_ROLE = 'org_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RolePayload2:
    r"""A role automatically applied to all users in an organization."""
    grants: List[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: RolePayload2Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    


class RolePayload1Type(str, Enum):
    USER_ROLE = 'user_role'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RolePayload1:
    r"""A standard user role. Must be explicitly assigned to users."""
    grants: List[shared_grant.Grant] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants') }})
    r"""List of grants (permissions) applied to the role"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Format: <organization_id>:<slug>"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Human-friendly name for the role"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""Id of an organization"""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly name for the role"""
    type: RolePayload1Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    



@dataclasses.dataclass
class RolePayload:
    pass
