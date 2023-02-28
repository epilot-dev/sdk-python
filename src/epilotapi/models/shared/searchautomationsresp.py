from __future__ import annotations
import dataclasses
from ..shared import automationflow as shared_automationflow
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchAutomationsResp:
    results: list[shared_automationflow.AutomationFlow] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    