"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from epilot_customer_portal.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class Effect(str, Enum):
    r"""Effect of the permission"""
    ALLOW = "allow"
    DENY = "deny"

class GrantTypedDict(TypedDict):
    action: str
    r"""Action for granting permission"""
    effect: NotRequired[Effect]
    r"""Effect of the permission"""
    resource: NotRequired[str]
    r"""Resource for granting permission"""
    

class Grant(BaseModel):
    action: str
    r"""Action for granting permission"""
    effect: Optional[Effect] = Effect.ALLOW
    r"""Effect of the permission"""
    resource: Optional[str] = None
    r"""Resource for granting permission"""
    
