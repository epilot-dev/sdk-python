"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class ReceivedEmailTriggerConfigurationMessageType(str, Enum):
    RECEIVED = 'RECEIVED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReceivedEmailTriggerConfiguration:
    message_type: Optional[ReceivedEmailTriggerConfigurationMessageType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message_type'), 'exclude': lambda f: f is None }})
    


class ReceivedEmailTriggerType(str, Enum):
    RECEIVED_EMAIL = 'received_email'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReceivedEmailTrigger:
    configuration: ReceivedEmailTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    type: ReceivedEmailTriggerType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    

