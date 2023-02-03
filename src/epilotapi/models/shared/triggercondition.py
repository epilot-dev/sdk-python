import dataclasses
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import comparison_enum as shared_comparison_enum


@dataclass_json
@dataclasses.dataclass
class TriggerCondition:
    comparison: shared_comparison_enum.ComparisonEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('comparison') }})
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    
