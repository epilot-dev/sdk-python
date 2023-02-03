import dataclasses
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class JourneySubmitTriggerConfiguration:
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id') }})
    
class JourneySubmitTriggerTypeEnum(str, Enum):
    JOURNEY_SUBMISSION = "journey_submission"


@dataclass_json
@dataclasses.dataclass
class JourneySubmitTrigger:
    configuration: JourneySubmitTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: JourneySubmitTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
