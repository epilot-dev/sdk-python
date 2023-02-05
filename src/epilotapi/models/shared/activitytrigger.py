import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional

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
    