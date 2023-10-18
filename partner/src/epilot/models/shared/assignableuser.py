"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssignableUserImageURI:
    original: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('original') }})
    thumbnail_32: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('thumbnail_32'), 'exclude': lambda f: f is None }})
    


class AssignableUserType(str, Enum):
    USER = 'user'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AssignableUser:
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name') }})
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    type: AssignableUserType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    image_uri: Optional[AssignableUserImageURI] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image_uri'), 'exclude': lambda f: f is None }})
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})
    

