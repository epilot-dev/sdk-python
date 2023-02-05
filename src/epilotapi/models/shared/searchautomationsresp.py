import dataclasses
from ..shared import automationflow as shared_automationflow
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class SearchAutomationsResp:
    results: list[shared_automationflow.AutomationFlow] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    