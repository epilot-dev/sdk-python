"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import itemtype_enum as shared_itemtype_enum
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class StepRequirementConditionEnum(str, Enum):
    CLOSED = "CLOSED"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StepRequirement:
    r"""describe the requirement for step enablement"""
    
    condition: StepRequirementConditionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('condition') }})  
    definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('definitionId') }})  
    type: shared_itemtype_enum.ItemTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    