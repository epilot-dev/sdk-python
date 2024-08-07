"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityAction:
    r"""An entity action configured from the entity schema"""
    action: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action') }})
    r"""A unique action name"""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    permission: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('permission'), 'exclude': lambda f: f is None }})
    r"""Permission required to show the action.
    If not provided, the action will be shown to all users.
    """
    

