"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from epilot_pricing.types import BaseModel
from typing import Any, Dict, List, Optional, TypedDict
from typing_extensions import NotRequired


class CheckResultsTypedDict(TypedDict):
    product_id: str
    matching_error: NotRequired[Dict[str, Any]]
    r"""A set of matching errors when checking availability"""
    matching_hits: NotRequired[float]
    r"""The number of rules matched"""
    

class CheckResults(BaseModel):
    product_id: str
    matching_error: Optional[Dict[str, Any]] = None
    r"""A set of matching errors when checking availability"""
    matching_hits: Optional[float] = None
    r"""The number of rules matched"""
    

class AvailabilityResultTypedDict(TypedDict):
    r"""The availability check result payload"""
    
    available_products: List[str]
    check_results: NotRequired[List[CheckResultsTypedDict]]
    r"""The check result details"""
    

class AvailabilityResult(BaseModel):
    r"""The availability check result payload"""
    
    available_products: List[str]
    check_results: Optional[List[CheckResults]] = None
    r"""The check result details"""
    