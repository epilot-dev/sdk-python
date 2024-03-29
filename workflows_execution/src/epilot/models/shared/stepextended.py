"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import automationconfig as shared_automationconfig
from ..shared import dynamicduedate as shared_dynamicduedate
from ..shared import ecpdetails as shared_ecpdetails
from ..shared import itemtype_enum as shared_itemtype_enum
from ..shared import steprequirement as shared_steprequirement
from ..shared import stepstatus_enum as shared_stepstatus_enum
from ..shared import steptype_enum as shared_steptype_enum
from ..shared import workflowcontext as shared_workflowcontext
from ..shared import workflowstatus_enum as shared_workflowstatus_enum
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StepExtended:
    
    entity_ref_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entityRefId') }})  
    execution_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executionId') }})  
    execution_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executionName') }})  
    execution_status: shared_workflowstatus_enum.WorkflowStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executionStatus') }})  
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    type: shared_itemtype_enum.ItemTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    assigned_to: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedTo'), 'exclude': lambda f: f is None }})  
    assigned_to_in_progress: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedToInProgress'), 'exclude': lambda f: f is None }})
    r"""The user which moved the step/task to the IN_PROGRESS state. The user should also be present in the assignedTo property of the step/task"""  
    automation_config: Optional[shared_automationconfig.AutomationConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('automationConfig'), 'exclude': lambda f: f is None }})
    r"""Configuration for automation execution to run"""  
    contexts: Optional[list[shared_workflowcontext.WorkflowContext]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contexts'), 'exclude': lambda f: f is None }})  
    created: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created'), 'exclude': lambda f: f is None }})  
    definition_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('definitionId'), 'exclude': lambda f: f is None }})  
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})  
    dynamic_due_date: Optional[shared_dynamicduedate.DynamicDueDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dynamicDueDate'), 'exclude': lambda f: f is None }})
    r"""set a Duedate for a step then a specific"""  
    ecp: Optional[shared_ecpdetails.ECPDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecp'), 'exclude': lambda f: f is None }})
    r"""Details regarding ECP for the workflow step"""  
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""enabled flag results from calculating the requirements"""  
    execution_type: Optional[shared_steptype_enum.StepTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executionType'), 'exclude': lambda f: f is None }})  
    last_updated: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastUpdated'), 'exclude': lambda f: f is None }})  
    manually_created: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manuallyCreated'), 'exclude': lambda f: f is None }})  
    requirements: Optional[list[shared_steprequirement.StepRequirement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requirements'), 'exclude': lambda f: f is None }})  
    section_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sectionId'), 'exclude': lambda f: f is None }})  
    status: Optional[shared_stepstatus_enum.StepStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})  
    user_ids: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIds'), 'exclude': lambda f: f is None }})
    r"""This field is deprecated. Please use assignedTo"""  
    