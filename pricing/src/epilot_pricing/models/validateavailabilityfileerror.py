"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_pricing.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ValidateAvailabilityFileErrorTypedDict(TypedDict):
    r"""The availability rule error"""
    
    msg: str
    r"""The error message"""
    data: NotRequired[str]
    r"""Data related to the error"""
    line: NotRequired[float]
    r"""The line number where the error was found"""
    

class ValidateAvailabilityFileError(BaseModel):
    r"""The availability rule error"""
    
    msg: str
    r"""The error message"""
    data: Optional[str] = None
    r"""Data related to the error"""
    line: Optional[float] = None
    r"""The line number where the error was found"""
    
