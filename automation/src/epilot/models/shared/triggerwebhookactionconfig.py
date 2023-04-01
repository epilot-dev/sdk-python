"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import triggerwebhookconfig as shared_triggerwebhookconfig
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class TriggerWebhookActionConfigTypeEnum(str, Enum):
    TRIGGER_WEBHOOK = 'trigger-webhook'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TriggerWebhookActionConfig:
    
    allow_failure: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_failure'), 'exclude': lambda f: f is None }})
    r"""Whether to stop execution in a failed state if this action fails"""  
    config: Optional[shared_triggerwebhookconfig.TriggerWebhookConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('config'), 'exclude': lambda f: f is None }})  
    created_automatically: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_automatically'), 'exclude': lambda f: f is None }})
    r"""Flag indicating whether the action was created automatically or manually"""  
    flow_action_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flow_action_id'), 'exclude': lambda f: f is None }})  
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    type: Optional[TriggerWebhookActionConfigTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})  
    