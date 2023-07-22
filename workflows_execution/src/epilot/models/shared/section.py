"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import itemtype as shared_itemtype
from ..shared import step as shared_step
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Section:
    r"""A group of Steps that define the progress of the Workflow"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name for this Section"""
    steps: list[shared_step.Step] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('steps') }})
    type: shared_itemtype.ItemType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    assigned_to: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignedTo'), 'exclude': lambda f: f is None }})
    definition_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('definitionId'), 'exclude': lambda f: f is None }})
    user_ids: Optional[list[float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIds'), 'exclude': lambda f: f is None }})
    r"""This field is deprecated. Please use assignedTo

    Deprecated: this field will be removed in a future release, please migrate away from it as soon as possible
    """
    

