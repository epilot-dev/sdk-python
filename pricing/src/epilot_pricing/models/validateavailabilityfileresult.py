"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .validateavailabilityfileerror import ValidateAvailabilityFileError, ValidateAvailabilityFileErrorTypedDict
from enum import Enum
from epilot_pricing.types import BaseModel
from typing import List, TypedDict


class Status(str, Enum):
    r"""The status of the validation"""
    SUCCESS = "success"
    ERROR = "error"

class ValidateAvailabilityFileResultTypedDict(TypedDict):
    r"""The availability map file result payload"""
    
    errors: List[ValidateAvailabilityFileErrorTypedDict]
    r"""The errors found on the file"""
    rules_parsed_count: float
    r"""The number of rules successfully parsed"""
    status: Status
    r"""The status of the validation"""
    

class ValidateAvailabilityFileResult(BaseModel):
    r"""The availability map file result payload"""
    
    errors: List[ValidateAvailabilityFileError]
    r"""The errors found on the file"""
    rules_parsed_count: float
    r"""The number of rules successfully parsed"""
    status: Status
    r"""The status of the validation"""
    