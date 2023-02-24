from __future__ import annotations
import dataclasses
from ..shared import comparison_enum as shared_comparison_enum
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerCondition:
    comparison: shared_comparison_enum.ComparisonEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('comparison') }})
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value'), 'exclude': lambda f: f is None }})
    