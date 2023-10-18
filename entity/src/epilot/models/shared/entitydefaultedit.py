"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultEditTableMenuOptions:
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label'), 'exclude': lambda f: f is None }})
    


class EntityDefaultEditViewType(str, Enum):
    DEFAULT = 'default'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultEdit:
    search_params: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_params'), 'exclude': lambda f: f is None }})
    summary_attributes: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary_attributes'), 'exclude': lambda f: f is None }})
    r"""List of attribute names that we show in the summary header"""
    table_menu_options: Optional[EntityDefaultEditTableMenuOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table_menu_options'), 'exclude': lambda f: f is None }})
    view_type: Optional[EntityDefaultEditViewType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_type'), 'exclude': lambda f: f is None }})
    

