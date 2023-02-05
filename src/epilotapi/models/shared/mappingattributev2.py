import dataclasses
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class MappingAttributeV2:
    operation: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('operation') }})
    target: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    