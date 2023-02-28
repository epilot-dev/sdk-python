from __future__ import annotations
import dataclasses
from ..shared import automationexecution as shared_automationexecution
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetExecutionsResp:
    results: list[shared_automationexecution.AutomationExecution] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    