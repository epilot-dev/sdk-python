"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class GrantEffectEnum(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Grant:
    
    action: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})  
    effect: Optional[GrantEffectEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('effect'), 'exclude': lambda f: f is None }})  
    resource: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource'), 'exclude': lambda f: f is None }})  
    