"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import itemtype_enum as shared_itemtype_enum
from ..shared import step as shared_step
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Section:
    r"""A group of Steps that define the progress of the Workflow"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    order: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order') }})  
    steps: list[shared_step.Step] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('steps') }})  
    type: shared_itemtype_enum.ItemTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})  
    