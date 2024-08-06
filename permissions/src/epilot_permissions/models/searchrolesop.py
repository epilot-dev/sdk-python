"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .role import Role, RoleTypedDict
from epilot_permissions.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class SearchRolesResponseBodyTypedDict(TypedDict):
    r"""ok"""
    
    hits: NotRequired[float]
    results: NotRequired[List[RoleTypedDict]]
    

class SearchRolesResponseBody(BaseModel):
    r"""ok"""
    
    hits: Optional[float] = None
    results: Optional[List[Role]] = None
    
