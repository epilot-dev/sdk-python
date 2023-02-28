from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JourneySubmitTriggerConfiguration:
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id') }})
    
class JourneySubmitTriggerTypeEnum(str, Enum):
    JOURNEY_SUBMISSION = "journey_submission"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JourneySubmitTrigger:
    configuration: JourneySubmitTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: JourneySubmitTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    