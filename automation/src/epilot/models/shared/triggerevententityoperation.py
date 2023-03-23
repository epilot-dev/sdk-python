"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import entityoperation_enum as shared_entityoperation_enum
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class TriggerEventEntityOperationTypeEnum(str, Enum):
    ENTITY_OPERATION = "entity_operation"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerEventEntityOperation:
    
    activity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activity_id') }})  
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id') }})  
    operation_type: shared_entityoperation_enum.EntityOperationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation_type') }})  
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})  
    type: Optional[TriggerEventEntityOperationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    