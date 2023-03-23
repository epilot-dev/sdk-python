"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import availabilitylocation as shared_availabilitylocation
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from epilot import utils
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AvailabilityFilters:
    r"""Availability filters dimensions"""
    
    location: shared_availabilitylocation.AvailabilityLocation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})  
    available_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""A value to be matched against the availability window (start & end date)"""  
    