"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any

class EqualsConditionOperationEnum(str, Enum):
    EQUALS = "equals"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EqualsCondition:
    r"""Check if attribute equals to any of the values"""
    
    attribute: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribute') }})  
    operation: EqualsConditionOperationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation') }})  
    values: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('values') }})  
    