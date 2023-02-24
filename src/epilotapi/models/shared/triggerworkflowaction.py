from __future__ import annotations
import dataclasses
from ..shared import erroroutput as shared_erroroutput
from ..shared import executionstatus_enum as shared_executionstatus_enum
from ..shared import retrystrategy_enum as shared_retrystrategy_enum
from ..shared import triggerworkflowconfig as shared_triggerworkflowconfig
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerWorkflowAction:
    allow_failure: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allow_failure'), 'exclude': lambda f: f is None }})
    config: Optional[shared_triggerworkflowconfig.TriggerWorkflowConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('config'), 'exclude': lambda f: f is None }})
    created_automatically: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_automatically'), 'exclude': lambda f: f is None }})
    error_output: Optional[shared_erroroutput.ErrorOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_output'), 'exclude': lambda f: f is None }})
    execution_status: Optional[shared_executionstatus_enum.ExecutionStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('execution_status'), 'exclude': lambda f: f is None }})
    flow_action_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('flow_action_id'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    outputs: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('outputs'), 'exclude': lambda f: f is None }})
    retry_strategy: Optional[shared_retrystrategy_enum.RetryStrategyEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('retry_strategy'), 'exclude': lambda f: f is None }})
    started_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('started_at'), 'exclude': lambda f: f is None }})
    type: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at'), 'exclude': lambda f: f is None }})
    