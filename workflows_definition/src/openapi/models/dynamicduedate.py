"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from openapi.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ActionTypeCondition(str, Enum):
    WORKFLOW_STARTED = "WORKFLOW_STARTED"
    STEP_CLOSED = "STEP_CLOSED"

class TimePeriod(str, Enum):
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"

class DynamicDueDateTypedDict(TypedDict):
    r"""set a Duedate for a step then a specific"""
    
    action_type_condition: ActionTypeCondition
    number_of_units: float
    time_period: TimePeriod
    step_id: NotRequired[str]
    

class DynamicDueDate(BaseModel):
    r"""set a Duedate for a step then a specific"""
    
    action_type_condition: Annotated[ActionTypeCondition, pydantic.Field(alias="actionTypeCondition")]
    number_of_units: Annotated[float, pydantic.Field(alias="numberOfUnits")]
    time_period: Annotated[TimePeriod, pydantic.Field(alias="timePeriod")]
    step_id: Annotated[Optional[str], pydantic.Field(alias="stepId")] = None
    
