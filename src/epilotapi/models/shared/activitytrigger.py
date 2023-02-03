import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

class ActivityTriggerConfigurationTypesEnum(str, Enum):
    CREATE_METER_READING = "CreateMeterReading"
    UPDATE_METER_READING = "UpdateMeterReading"
    MESSAGE_ACTIVITY = "MessageActivity"
    SYNC_ACTIVITY = "SyncActivity"


@dataclass_json
@dataclasses.dataclass
class ActivityTriggerConfiguration:
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema') }})
    types: Optional[list[ActivityTriggerConfigurationTypesEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('types') }})
    
class ActivityTriggerTypeEnum(str, Enum):
    ACTIVITY = "activity"


@dataclass_json
@dataclasses.dataclass
class ActivityTrigger:
    configuration: ActivityTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: ActivityTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
