"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class PartnerStatus(str, Enum):
    PENDING = 'Pending'
    REQUEST = 'Request'
    DELETED = 'Deleted'
    INVITED = 'Invited'
    REJECTED = 'Rejected'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Partner:
    r"""Partner"""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_name'), 'exclude': lambda f: f is None }})
    r"""Company name"""
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Description"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    invitation_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invitation_email'), 'exclude': lambda f: f is None }})
    r"""Email using to receive invitation"""
    invitation_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invitation_token'), 'exclude': lambda f: f is None }})
    r"""Invitation token"""
    organization_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id'), 'exclude': lambda f: f is None }})
    partner_org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partner_org_id'), 'exclude': lambda f: f is None }})
    r"""Target Organization"""
    signed_up_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signed_up_email'), 'exclude': lambda f: f is None }})
    r"""Email using to sign up"""
    status: Optional[PartnerStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

