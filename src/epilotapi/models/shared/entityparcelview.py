from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional

class EntityParcelViewViewTypeEnum(str, Enum):
    PARCEL = "parcel"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityParcelView:
    import_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('import'), 'exclude': lambda f: f is None }})
    view_type: Optional[EntityParcelViewViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type'), 'exclude': lambda f: f is None }})
    