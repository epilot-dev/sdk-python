"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_customer_portal.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class GetValidSecondaryAttributesDataTypedDict(TypedDict):
    name: NotRequired[str]
    r"""Name of the secondary attribute"""
    type: NotRequired[str]
    r"""Type of the secondary attribute"""
    

class GetValidSecondaryAttributesData(BaseModel):
    name: Optional[str] = None
    r"""Name of the secondary attribute"""
    type: Optional[str] = None
    r"""Type of the secondary attribute"""
    

class GetValidSecondaryAttributesResponseBodyTypedDict(TypedDict):
    r"""Valid secondary attributes for the contact entity are returned successfully."""
    
    data: NotRequired[List[GetValidSecondaryAttributesDataTypedDict]]
    

class GetValidSecondaryAttributesResponseBody(BaseModel):
    r"""Valid secondary attributes for the contact entity are returned successfully."""
    
    data: Optional[List[GetValidSecondaryAttributesData]] = None
    
