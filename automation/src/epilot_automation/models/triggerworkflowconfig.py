"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assignuserstostep import AssignUsersToStep, AssignUsersToStepTypedDict
from .triggerworkflowcondition import TriggerWorkflowCondition, TriggerWorkflowConditionTypedDict
from epilot_automation.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class TriggerWorkflowConfigTypedDict(TypedDict):
    assign_steps: NotRequired[List[AssignUsersToStepTypedDict]]
    assignees: NotRequired[List[str]]
    conditions: NotRequired[List[TriggerWorkflowConditionTypedDict]]
    target_workflow: NotRequired[str]
    

class TriggerWorkflowConfig(BaseModel):
    assign_steps: Optional[List[AssignUsersToStep]] = None
    assignees: Optional[List[str]] = None
    conditions: Optional[List[TriggerWorkflowCondition]] = None
    target_workflow: Optional[str] = None
    
