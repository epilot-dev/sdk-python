from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultEditTableMenuOptions:
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon'), 'exclude': lambda f: f is None }})
    label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('label'), 'exclude': lambda f: f is None }})
    
class EntityDefaultEditViewTypeEnum(str, Enum):
    DEFAULT = "default"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultEdit:
    search_params: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('search_params'), 'exclude': lambda f: f is None }})
    table_menu_options: Optional[EntityDefaultEditTableMenuOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_menu_options'), 'exclude': lambda f: f is None }})
    view_type: Optional[EntityDefaultEditViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type'), 'exclude': lambda f: f is None }})
    