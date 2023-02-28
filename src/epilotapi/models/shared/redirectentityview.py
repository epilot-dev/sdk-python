from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional

class RedirectEntityViewViewTypeEnum(str, Enum):
    REDIRECT = "redirect"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RedirectEntityView:
    route: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('route'), 'exclude': lambda f: f is None }})
    view_type: Optional[RedirectEntityViewViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type'), 'exclude': lambda f: f is None }})
    