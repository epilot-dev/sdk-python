"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class EntityViewDisabledViewTypeEnum(str, Enum):
    DISABLED = 'disabled'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityViewDisabled:
    
    view_type: Optional[EntityViewDisabledViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_type'), 'exclude': lambda f: f is None }})  
    