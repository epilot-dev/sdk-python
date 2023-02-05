import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class EntityManualTriggerConfiguration:
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema') }})
    
class EntityManualTriggerTypeEnum(str, Enum):
    ENTITY_MANUAL = "entity_manual"


@dataclass_json
@dataclasses.dataclass
class EntityManualTrigger:
    configuration: EntityManualTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: EntityManualTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    