from __future__ import annotations
import dataclasses
from ..shared import mappingattributemode_enum as shared_mappingattributemode_enum
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SetValueMapper:
    mode: shared_mappingattributemode_enum.MappingAttributeModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('mode') }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    value: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    