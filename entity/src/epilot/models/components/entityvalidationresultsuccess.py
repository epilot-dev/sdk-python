"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .entityvalidationerror import EntityValidationError
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import List

class Status(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityValidationResultSuccess:
    r"""Validation result for a successful validation"""
    errors: List[EntityValidationError] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors') }})
    status: Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

