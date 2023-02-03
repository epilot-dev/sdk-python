import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import mappingattributemode_enum as shared_mappingattributemode_enum


@dataclass_json
@dataclasses.dataclass
class AppendValueMapper:
    mode: shared_mappingattributemode_enum.MappingAttributeModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('mode') }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    value_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value_json') }})
    source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    target_unique: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_unique') }})
    
