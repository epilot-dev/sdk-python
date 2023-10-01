"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import grant as shared_grant
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from epilot import utils
from typing import Final, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UserRole:
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
    TYPE: Final[str] = dataclasses.field(default='user_role', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""date and time then the role will expire"""
    

