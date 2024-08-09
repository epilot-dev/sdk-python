"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .automationconfig import AutomationConfig, AutomationConfigTypedDict
from .stepstatus import StepStatus
from .steptype import StepType
from epilot_workflows_execution.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateStepReqTypedDict(TypedDict):
    name: str
    automation_config: NotRequired[AutomationConfigTypedDict]
    r"""Configuration for automation execution to run"""
    execution_type: NotRequired[StepType]
    insertion_index: NotRequired[float]
    section_id: NotRequired[str]
    status: NotRequired[StepStatus]
    

class CreateStepReq(BaseModel):
    name: str
    automation_config: Annotated[Optional[AutomationConfig], pydantic.Field(alias="automationConfig")] = None
    r"""Configuration for automation execution to run"""
    execution_type: Annotated[Optional[StepType], pydantic.Field(alias="executionType")] = None
    insertion_index: Annotated[Optional[float], pydantic.Field(alias="insertionIndex")] = 0
    section_id: Annotated[Optional[str], pydantic.Field(alias="sectionId")] = None
    status: Optional[StepStatus] = None
    
