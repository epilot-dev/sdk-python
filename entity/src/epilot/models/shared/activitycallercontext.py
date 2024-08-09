"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityCallerContextEpilotAuthToken:
    cognito_username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cognito:username'), 'exclude': lambda f: f is None }})
    custom_ivy_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom:ivy_user_id'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    sub: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sub'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityCallerContextEpilotAuth:
    token: Optional[ActivityCallerContextEpilotAuthToken] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityCallerContext:
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    epilot_auth: Optional[ActivityCallerContextEpilotAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('EpilotAuth'), 'exclude': lambda f: f is None }})
    
