"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityManualTriggerConfiguration:
    
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""Which entity type can this automation be triggered from"""
    
class EntityManualTriggerType(str, Enum):
    ENTITY_MANUAL = 'entity_manual'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityManualTrigger:
    
    configuration: EntityManualTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration') }})
    type: EntityManualTriggerType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    