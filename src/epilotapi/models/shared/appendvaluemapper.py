from __future__ import annotations
import dataclasses
from ..shared import mappingattributemode_enum as shared_mappingattributemode_enum
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppendValueMapper:
    mode: shared_mappingattributemode_enum.MappingAttributeModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('mode') }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    value_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value_json') }})
    source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source'), 'exclude': lambda f: f is None }})
    target_unique: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_unique'), 'exclude': lambda f: f is None }})
    