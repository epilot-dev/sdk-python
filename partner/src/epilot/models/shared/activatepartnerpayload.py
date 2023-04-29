"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivatePartnerPayload:
    
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""organization id"""
    signed_up_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signed_up_email') }})
    r"""Email using to sign up"""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company_name'), 'exclude': lambda f: f is None }})
    r"""Company name"""
    