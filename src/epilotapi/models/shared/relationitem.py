from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationItem:
    attribute: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('attribute') }})
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_id') }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_tags'), 'exclude': lambda f: f is None }})
    reverse: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reverse'), 'exclude': lambda f: f is None }})
    