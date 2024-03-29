"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import closingreasonid as shared_closingreasonid
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClosingReasonsIds:
    r"""Returns the entire catalog of closing reasons for a specific workflow"""
    
    reasons: list[shared_closingreasonid.ClosingReasonID] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reasons') }})  
    