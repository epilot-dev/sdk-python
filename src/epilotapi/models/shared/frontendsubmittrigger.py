import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class FrontendSubmitTriggerConfiguration:
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id') }})
    
class FrontendSubmitTriggerTypeEnum(str, Enum):
    FRONTEND_SUBMISSION = "frontend_submission"


@dataclass_json
@dataclasses.dataclass
class FrontendSubmitTrigger:
    configuration: FrontendSubmitTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: FrontendSubmitTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    