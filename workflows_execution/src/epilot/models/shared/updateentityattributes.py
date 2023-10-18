"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils

class UpdateEntityAttributesSource(str, Enum):
    WORKFLOW_STATUS = 'workflow_status'
    CURRENT_SECTION = 'current_section'
    CURRENT_STEP = 'current_step'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateEntityAttributesTarget:
    entity_attribute: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entityAttribute') }})
    entity_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entitySchema') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateEntityAttributes:
    source: UpdateEntityAttributesSource = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    target: UpdateEntityAttributesTarget = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target') }})
    

