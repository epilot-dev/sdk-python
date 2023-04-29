"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class ActivityTriggerConfigurationTypesEnum(str, Enum):
    CREATE_METER_READING = 'CreateMeterReading'
    UPDATE_METER_READING = 'UpdateMeterReading'
    MESSAGE_ACTIVITY = 'MessageActivity'
    SYNC_ACTIVITY = 'SyncActivity'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityTriggerConfiguration:
    
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    types: Optional[list[ActivityTriggerConfigurationTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('types'), 'exclude': lambda f: f is None }})
    
class ActivityTriggerTypeEnum(str, Enum):
    ACTIVITY = 'activity'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityTrigger:
    
    configuration: ActivityTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    type: ActivityTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    