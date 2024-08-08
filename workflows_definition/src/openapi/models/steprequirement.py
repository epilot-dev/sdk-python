"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .itemtype import ItemType
from enum import Enum
from openapi.types import BaseModel
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class Condition(str, Enum):
    CLOSED = "CLOSED"

class StepRequirementTypedDict(TypedDict):
    r"""describe the requirement for step enablement"""
    
    condition: Condition
    definition_id: str
    type: ItemType
    

class StepRequirement(BaseModel):
    r"""describe the requirement for step enablement"""
    
    condition: Condition
    definition_id: Annotated[str, pydantic.Field(alias="definitionId")]
    type: ItemType
    
