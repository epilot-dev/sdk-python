"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import closingreason as shared_closingreason
from ..shared import dynamicduedate as shared_dynamicduedate
from ..shared import section as shared_section
from ..shared import step as shared_step
from ..shared import stepid as shared_stepid
from ..shared import triggertype as shared_triggertype
from ..shared import updateentityattributes as shared_updateentityattributes
from ..shared import workflowcontext as shared_workflowcontext
from ..shared import workflowstatus as shared_workflowstatus
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import List, Optional, Union


@dataclasses.dataclass
class WorkflowExecutionFlow:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkflowExecution:
    flow: List[Union[shared_section.Section, shared_step.Step]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flow') }})
    assigned_to: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedTo'), 'exclude': lambda f: f is None }})
    closing_reason_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('closingReasonDescription'), 'exclude': lambda f: f is None }})
    completed_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completedTime'), 'exclude': lambda f: f is None }})
    r"""Completed time of the workflow execution"""
    configured_closing_reason_snapshot: Optional[List[shared_closingreason.ClosingReason]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuredClosingReasonSnapshot'), 'exclude': lambda f: f is None }})
    contexts: Optional[List[shared_workflowcontext.WorkflowContext]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contexts'), 'exclude': lambda f: f is None }})
    creation_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime'), 'exclude': lambda f: f is None }})
    r"""Creation timestamp which will double as started time as well"""
    definition_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('definitionId'), 'exclude': lambda f: f is None }})
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})
    r"""Due date for finishing the workflow"""
    dynamic_due_date: Optional[shared_dynamicduedate.DynamicDueDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dynamicDueDate'), 'exclude': lambda f: f is None }})
    r"""set a Duedate for a step then a specific"""
    enable_ecp_workflow: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableECPWorkflow'), 'exclude': lambda f: f is None }})
    r"""Indicates whether this workflow is available for End Customer Portal or not. By default it's not."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    last_modified_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastModifiedBy'), 'exclude': lambda f: f is None }})
    r"""Id of the user who closed workflow"""
    last_update_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastUpdateTime'), 'exclude': lambda f: f is None }})
    r"""Last Update timestamp"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    next_open_step: Optional[shared_stepid.StepID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nextOpenStep'), 'exclude': lambda f: f is None }})
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId'), 'exclude': lambda f: f is None }})
    selected_closing_reasons: Optional[List[shared_closingreason.ClosingReason]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedClosingReasons'), 'exclude': lambda f: f is None }})
    status: Optional[shared_workflowstatus.WorkflowStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    trigger: Optional[shared_triggertype.TriggerType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trigger'), 'exclude': lambda f: f is None }})
    update_entity_attributes: Optional[List[shared_updateentityattributes.UpdateEntityAttributes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateEntityAttributes'), 'exclude': lambda f: f is None }})
    version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    r"""Version of the workflow execution"""
    

