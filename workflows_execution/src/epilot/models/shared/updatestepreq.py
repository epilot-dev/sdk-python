"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import automationconfig as shared_automationconfig
from ..shared import dynamicduedate as shared_dynamicduedate
from ..shared import steppositionat as shared_steppositionat
from ..shared import stepstatus as shared_stepstatus
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateStepReq:
    r"""Workflow Execution Step payload"""
    entity_ref_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entityRefId') }})
    assigned_to: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedTo'), 'exclude': lambda f: f is None }})
    assigned_to_in_progress: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedToInProgress'), 'exclude': lambda f: f is None }})
    r"""The user which moved the step/task to the IN_PROGRESS state. The user should also be present in the assignedTo property of the step/task"""
    automation_config: Optional[shared_automationconfig.AutomationConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('automationConfig'), 'exclude': lambda f: f is None }})
    r"""Configuration for automation execution to run"""
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})
    dynamic_due_date: Optional[shared_dynamicduedate.DynamicDueDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dynamicDueDate'), 'exclude': lambda f: f is None }})
    r"""set a Duedate for a step then a specific"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    position: Optional[shared_steppositionat.StepPositionAt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('position'), 'exclude': lambda f: f is None }})
    status: Optional[shared_stepstatus.StepStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    user_ids: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIds'), 'exclude': lambda f: f is None }})
    r"""This field is deprecated. Please use assignedTo"""
    

