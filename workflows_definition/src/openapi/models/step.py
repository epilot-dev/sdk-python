"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dynamicduedate import DynamicDueDate, DynamicDueDateTypedDict
from .ecpdetails import ECPDetails, ECPDetailsTypedDict
from .itemtype import ItemType
from .stepdescription import StepDescription, StepDescriptionTypedDict
from .stepjourney import StepJourney, StepJourneyTypedDict
from .steprequirement import StepRequirement, StepRequirementTypedDict
from .steptype import StepType
from openapi.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AutomationConfigTypedDict(TypedDict):
    flow_id: str
    r"""Id of the configured automation to run"""
    

class AutomationConfig(BaseModel):
    flow_id: Annotated[str, pydantic.Field(alias="flowId")]
    r"""Id of the configured automation to run"""
    

class StepTypedDict(TypedDict):
    r"""Action that needs to be done in a Workflow"""
    
    name: str
    order: float
    type: ItemType
    assigned_to: NotRequired[List[str]]
    automation_config: NotRequired[AutomationConfigTypedDict]
    description: NotRequired[StepDescriptionTypedDict]
    r"""Longer information regarding Task"""
    due_date: NotRequired[str]
    dynamic_due_date: NotRequired[DynamicDueDateTypedDict]
    r"""set a Duedate for a step then a specific"""
    ecp: NotRequired[ECPDetailsTypedDict]
    r"""Details regarding ECP for the workflow step"""
    execution_type: NotRequired[StepType]
    id: NotRequired[str]
    installer: NotRequired[ECPDetailsTypedDict]
    r"""Details regarding ECP for the workflow step"""
    journey: NotRequired[StepJourneyTypedDict]
    requirements: NotRequired[List[StepRequirementTypedDict]]
    r"""requirements that need to be fulfilled in order to enable the step execution"""
    user_ids: NotRequired[List[float]]
    r"""This field is deprecated. Please use assignedTo"""
    

class Step(BaseModel):
    r"""Action that needs to be done in a Workflow"""
    
    name: str
    order: float
    type: ItemType
    assigned_to: Annotated[Optional[List[str]], pydantic.Field(alias="assignedTo")] = None
    automation_config: Annotated[Optional[AutomationConfig], pydantic.Field(alias="automationConfig")] = None
    description: Optional[StepDescription] = None
    r"""Longer information regarding Task"""
    due_date: Annotated[Optional[str], pydantic.Field(alias="dueDate")] = None
    dynamic_due_date: Annotated[Optional[DynamicDueDate], pydantic.Field(alias="dynamicDueDate")] = None
    r"""set a Duedate for a step then a specific"""
    ecp: Optional[ECPDetails] = None
    r"""Details regarding ECP for the workflow step"""
    execution_type: Annotated[Optional[StepType], pydantic.Field(alias="executionType")] = None
    id: Optional[str] = None
    installer: Optional[ECPDetails] = None
    r"""Details regarding ECP for the workflow step"""
    journey: Optional[StepJourney] = None
    requirements: Optional[List[StepRequirement]] = None
    r"""requirements that need to be fulfilled in order to enable the step execution"""
    user_ids: Annotated[Optional[List[float]], pydantic.Field(deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.", alias="userIds")] = None
    r"""This field is deprecated. Please use assignedTo"""
    
