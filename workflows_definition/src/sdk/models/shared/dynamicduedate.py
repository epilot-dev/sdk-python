"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class DynamicDueDateActionTypeCondition(str, Enum):
    WORKFLOW_STARTED = 'WORKFLOW_STARTED'
    STEP_CLOSED = 'STEP_CLOSED'

class DynamicDueDateTimePeriod(str, Enum):
    DAYS = 'days'
    WEEKS = 'weeks'
    MONTHS = 'months'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DynamicDueDate:
    r"""set a Duedate for a step then a specific"""
    action_type_condition: DynamicDueDateActionTypeCondition = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actionTypeCondition') }})
    number_of_units: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numberOfUnits') }})
    time_period: DynamicDueDateTimePeriod = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timePeriod') }})
    step_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stepId'), 'exclude': lambda f: f is None }})
    

