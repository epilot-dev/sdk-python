"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_permissions.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class AssignmentTypedDict(TypedDict):
    r"""A role attached to an user"""
    
    roles: NotRequired[List[str]]
    user_id: NotRequired[str]
    r"""Id of a user"""
    

class Assignment(BaseModel):
    r"""A role attached to an user"""
    
    roles: Optional[List[str]] = None
    user_id: Optional[str] = None
    r"""Id of a user"""
    
