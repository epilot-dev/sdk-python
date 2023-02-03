import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class APISubmissionTriggerConfiguration:
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id') }})
    
class APISubmissionTriggerTypeEnum(str, Enum):
    API_SUBMISSION = "api_submission"


@dataclass_json
@dataclasses.dataclass
class APISubmissionTrigger:
    configuration: APISubmissionTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: APISubmissionTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
