"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import assignuserstostep as shared_assignuserstostep
from ..shared import triggerworkflowcondition as shared_triggerworkflowcondition
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerWorkflowConfig:
    
    assign_steps: Optional[list[shared_assignuserstostep.AssignUsersToStep]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assign_steps'), 'exclude': lambda f: f is None }})  
    assignees: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignees'), 'exclude': lambda f: f is None }})  
    conditions: Optional[list[shared_triggerworkflowcondition.TriggerWorkflowCondition]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conditions'), 'exclude': lambda f: f is None }})  
    target_workflow: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_workflow'), 'exclude': lambda f: f is None }})  
    