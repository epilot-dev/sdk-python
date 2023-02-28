from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultTableDropdownItems:
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag'), 'exclude': lambda f: f is None }})
    legacy: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('legacy'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultTableNavbarActionsOptions:
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    params: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('params'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultTableNavbarActions:
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    options: Optional[list[EntityDefaultTableNavbarActionsOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options'), 'exclude': lambda f: f is None }})
    
class EntityDefaultTableViewTypeEnum(str, Enum):
    DEFAULT = "default"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultTable:
    classic_view: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classic_view'), 'exclude': lambda f: f is None }})
    dropdown_items: Optional[list[EntityDefaultTableDropdownItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dropdown_items'), 'exclude': lambda f: f is None }})
    enable_thumbnails: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_thumbnails'), 'exclude': lambda f: f is None }})
    navbar_actions: Optional[list[EntityDefaultTableNavbarActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('navbar_actions'), 'exclude': lambda f: f is None }})
    row_actions: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('row_actions'), 'exclude': lambda f: f is None }})
    view_type: Optional[EntityDefaultTableViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type'), 'exclude': lambda f: f is None }})
    