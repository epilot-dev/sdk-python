from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MappingConfigRef:
    config_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('config_id') }})
    target_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_id') }})
    version: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('version'), 'exclude': lambda f: f is None }})
    