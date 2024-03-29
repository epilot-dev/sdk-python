"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import userdetail as shared_userdetail
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any, Optional

class SignupUserPayloadLanguageEnum(str, Enum):
    r"""Language for user invitation email"""
    EN = "en"
    DE = "de"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SignupUserPayload:
    
    language: Optional[SignupUserPayloadLanguageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})
    r"""Language for user invitation email"""  
    organization_detail: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_detail'), 'exclude': lambda f: f is None }})  
    user_detail: Optional[shared_userdetail.UserDetail] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_detail'), 'exclude': lambda f: f is None }})  
    