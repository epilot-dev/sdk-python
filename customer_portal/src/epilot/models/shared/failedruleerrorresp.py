"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional



@dataclasses.dataclass
class FailedRuleErrorRespFailedRule:
    r"""Failed validation rule"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FailedRuleErrorResp:
    failed_rule: Optional[FailedRuleErrorRespFailedRule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_rule'), 'exclude': lambda f: f is None }})
    r"""Failed validation rule"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Error message"""
    

