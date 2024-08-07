"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any, Dict, List, Optional, Union

class SavedViewCreatedBy2Source(str, Enum):
    SYSTEM = 'SYSTEM'
    BLUEPRINT = 'BLUEPRINT'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavedViewCreatedBy2:
    r"""A system-created view"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    source: Optional[SavedViewCreatedBy2Source] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavedViewCreatedBy1:
    r"""A user that created the view"""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class SavedViewCreatedBy:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavedView:
    r"""A saved entity view"""
    created_by: Union[SavedViewCreatedBy1, SavedViewCreatedBy2] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""User-friendly identifier for the saved view"""
    slug: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""list of schemas a view can belong to"""
    ui_config: Dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ui_config') }})
    is_favorited_by: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isFavoritedBy'), 'exclude': lambda f: f is None }})
    r"""List of users (IDs) that have favorited the view"""
    org: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org'), 'exclude': lambda f: f is None }})
    r"""Organisation ID a view belongs to"""
    shared: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shared'), 'exclude': lambda f: f is None }})
    r"""boolean property for if a view is shared with organisation"""
    

