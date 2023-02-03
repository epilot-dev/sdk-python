import dataclasses
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import automationexecution as shared_automationexecution


@dataclass_json
@dataclasses.dataclass
class GetExecutionsResp:
    results: list[shared_automationexecution.AutomationExecution] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    
