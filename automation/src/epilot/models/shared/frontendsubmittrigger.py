"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FrontendSubmitTriggerConfiguration:
    
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id'), 'exclude': lambda f: f is None }})  
    
class FrontendSubmitTriggerTypeEnum(str, Enum):
    FRONTEND_SUBMISSION = "frontend_submission"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FrontendSubmitTrigger:
    
    configuration: FrontendSubmitTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})  
    type: FrontendSubmitTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    