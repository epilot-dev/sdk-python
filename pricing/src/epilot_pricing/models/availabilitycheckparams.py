"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .availabilityfilters import AvailabilityFilters, AvailabilityFiltersTypedDict
from epilot_pricing.types import BaseModel
from typing import List, TypedDict


class AvailabilityCheckParamsTypedDict(TypedDict):
    r"""Availability check request payload"""
    
    filters: AvailabilityFiltersTypedDict
    r"""Availability filters dimensions"""
    products: List[str]
    r"""Products to check availability"""
    

class AvailabilityCheckParams(BaseModel):
    r"""Availability check request payload"""
    
    filters: AvailabilityFilters
    r"""Availability filters dimensions"""
    products: List[str]
    r"""Products to check availability"""
    