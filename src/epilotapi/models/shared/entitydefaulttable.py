import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class EntityDefaultTableDropdownItems:
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    legacy: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('legacy') }})
    

@dataclass_json
@dataclasses.dataclass
class EntityDefaultTableNavbarActionsOptions:
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    params: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('params') }})
    

@dataclass_json
@dataclasses.dataclass
class EntityDefaultTableNavbarActions:
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    options: Optional[list[EntityDefaultTableNavbarActionsOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    
class EntityDefaultTableViewTypeEnum(str, Enum):
    DEFAULT = "default"


@dataclass_json
@dataclasses.dataclass
class EntityDefaultTable:
    classic_view: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('classic_view') }})
    dropdown_items: Optional[list[EntityDefaultTableDropdownItems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dropdown_items') }})
    enable_thumbnails: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_thumbnails') }})
    navbar_actions: Optional[list[EntityDefaultTableNavbarActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('navbar_actions') }})
    row_actions: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('row_actions') }})
    view_type: Optional[EntityDefaultTableViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type') }})
    