"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import closingreasonid as shared_closingreasonid
from ..shared import dynamicduedate as shared_dynamicduedate
from ..shared import updateentityattributes as shared_updateentityattributes
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkflowDefinition:
    r"""Workflow Definition payload"""
    
    flow: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flow') }})  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    assigned_to: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedTo'), 'exclude': lambda f: f is None }})  
    closing_reasons: Optional[list[shared_closingreasonid.ClosingReasonID]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('closingReasons'), 'exclude': lambda f: f is None }})  
    creation_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime'), 'exclude': lambda f: f is None }})
    r"""ISO String Date & Time"""  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})  
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})  
    dynamic_due_date: Optional[shared_dynamicduedate.DynamicDueDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dynamicDueDate'), 'exclude': lambda f: f is None }})
    r"""set a Duedate for a step then a specific"""  
    enable_ecp_workflow: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableECPWorkflow'), 'exclude': lambda f: f is None }})
    r"""Indicates whether this workflow is available for End Customer Portal or not. By default it's not."""  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})  
    last_update_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastUpdateTime'), 'exclude': lambda f: f is None }})
    r"""ISO String Date & Time"""  
    update_entity_attributes: Optional[list[shared_updateentityattributes.UpdateEntityAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateEntityAttributes'), 'exclude': lambda f: f is None }})  
    user_ids: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIds'), 'exclude': lambda f: f is None }})
    r"""This field is deprecated. Please use assignedTo"""  
    