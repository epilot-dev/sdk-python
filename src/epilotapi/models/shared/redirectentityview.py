import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional

class RedirectEntityViewViewTypeEnum(str, Enum):
    REDIRECT = "redirect"


@dataclass_json
@dataclasses.dataclass
class RedirectEntityView:
    route: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('route') }})
    view_type: Optional[RedirectEntityViewViewTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view_type') }})
    