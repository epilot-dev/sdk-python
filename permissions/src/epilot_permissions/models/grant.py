"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .grantcondition import GrantCondition, GrantConditionTypedDict
from enum import Enum
from epilot_permissions.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class Effect(str, Enum):
    ALLOW = "allow"
    DENY = "deny"

class GrantTypedDict(TypedDict):
    action: str
    conditions: NotRequired[List[GrantConditionTypedDict]]
    effect: NotRequired[Effect]
    resource: NotRequired[str]
    

class Grant(BaseModel):
    action: str
    conditions: Optional[List[GrantCondition]] = None
    effect: Optional[Effect] = Effect.ALLOW
    resource: Optional[str] = None
    
