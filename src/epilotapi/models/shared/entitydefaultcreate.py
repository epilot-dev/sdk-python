import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class EntityDefaultCreateTableMenuOptions:
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }})
    label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    
class EntityDefaultCreateViewTypeEnum(str, Enum):
    DEFAULT = "default"


@dataclass_json
@dataclasses.dataclass
class EntityDefaultCreate:
    search_params: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('search_params') }})
    table_menu_options: Optional[EntityDefaultCreateTableMenuOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_menu_options') }})
    view_type: Optional[EntityDefaultCreateViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type') }})
    