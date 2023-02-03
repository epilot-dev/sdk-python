import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

class ReceivedEmailTriggerConfigurationMessageTypeEnum(str, Enum):
    RECEIVED = "RECEIVED"


@dataclass_json
@dataclasses.dataclass
class ReceivedEmailTriggerConfiguration:
    message_type: Optional[ReceivedEmailTriggerConfigurationMessageTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message_type') }})
    
class ReceivedEmailTriggerTypeEnum(str, Enum):
    RECEIVED_EMAIL = "received_email"


@dataclass_json
@dataclasses.dataclass
class ReceivedEmailTrigger:
    configuration: ReceivedEmailTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: ReceivedEmailTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
