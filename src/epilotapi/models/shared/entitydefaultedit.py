import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class EntityDefaultEditTableMenuOptions:
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }})
    label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    
class EntityDefaultEditViewTypeEnum(str, Enum):
    DEFAULT = "default"


@dataclass_json
@dataclasses.dataclass
class EntityDefaultEdit:
    search_params: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('search_params') }})
    table_menu_options: Optional[EntityDefaultEditTableMenuOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_menu_options') }})
    view_type: Optional[EntityDefaultEditViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type') }})
    