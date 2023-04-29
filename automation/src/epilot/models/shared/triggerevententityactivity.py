"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class TriggerEventEntityActivityTypeEnum(str, Enum):
    ENTITY_ACTIVITY = 'entity_activity'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerEventEntityActivity:
    
    activity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activity_id') }})
    activity_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activity_type') }})
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id'), 'exclude': lambda f: f is None }})
    type: Optional[TriggerEventEntityActivityTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    