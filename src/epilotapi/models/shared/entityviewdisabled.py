import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

class EntityViewDisabledViewTypeEnum(str, Enum):
    DISABLED = "disabled"


@dataclass_json
@dataclasses.dataclass
class EntityViewDisabled:
    view_type: Optional[EntityViewDisabledViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type') }})
    
