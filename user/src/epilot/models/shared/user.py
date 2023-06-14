"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UserProperties:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class User:
    r"""Currently logged in user"""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Deprecated: this field will be removed in a future release, please migrate away from it as soon as possible"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    preferred_language: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preferred_language') }})
    properties: list[UserProperties] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties') }})
    roles: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('roles') }})
    r"""Deprecated! Please use Permissions API instead
    
    Deprecated: this field will be removed in a future release, please migrate away from it as soon as possible
    """
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name'), 'exclude': lambda f: f is None }})
    r"""Deprecated: this field will be removed in a future release, please migrate away from it as soon as possible"""
    image_uri: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image_uri'), 'exclude': lambda f: f is None }})
    signature: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signature'), 'exclude': lambda f: f is None }})
    

