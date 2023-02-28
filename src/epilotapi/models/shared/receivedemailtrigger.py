from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional

class ReceivedEmailTriggerConfigurationMessageTypeEnum(str, Enum):
    RECEIVED = "RECEIVED"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReceivedEmailTriggerConfiguration:
    message_type: Optional[ReceivedEmailTriggerConfigurationMessageTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message_type'), 'exclude': lambda f: f is None }})
    
class ReceivedEmailTriggerTypeEnum(str, Enum):
    RECEIVED_EMAIL = "received_email"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReceivedEmailTrigger:
    configuration: ReceivedEmailTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: ReceivedEmailTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    