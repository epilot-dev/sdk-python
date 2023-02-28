from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APISubmissionTriggerConfiguration:
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id'), 'exclude': lambda f: f is None }})
    
class APISubmissionTriggerTypeEnum(str, Enum):
    API_SUBMISSION = "api_submission"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APISubmissionTrigger:
    configuration: APISubmissionTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: APISubmissionTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    