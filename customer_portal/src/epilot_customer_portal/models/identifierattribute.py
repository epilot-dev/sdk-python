"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_customer_portal.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class IdentifierAttributeTypedDict(TypedDict):
    label: NotRequired[str]
    r"""Label attribute"""
    name: NotRequired[str]
    r"""Name of the attribute"""
    type: NotRequired[str]
    r"""Type of the secondary attribute"""
    

class IdentifierAttribute(BaseModel):
    label: Optional[str] = None
    r"""Label attribute"""
    name: Optional[str] = None
    r"""Name of the attribute"""
    type: Optional[str] = None
    r"""Type of the secondary attribute"""
    
