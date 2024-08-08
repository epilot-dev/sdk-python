"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_template_variables.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CategoryResultTypedDict(TypedDict):
    category: NotRequired[str]
    description: NotRequired[str]
    

class CategoryResult(BaseModel):
    category: Optional[str] = None
    description: Optional[str] = None
    
