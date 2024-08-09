"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_automation.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class WildcardConditionTypedDict(TypedDict):
    wildcard: NotRequired[str]
    

class WildcardCondition(BaseModel):
    wildcard: Optional[str] = None
    
