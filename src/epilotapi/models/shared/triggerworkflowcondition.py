import dataclasses
from ..shared import comparison_enum as shared_comparison_enum
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class TriggerWorkflowCondition:
    comparison: shared_comparison_enum.ComparisonEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('comparison') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema') }})
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    