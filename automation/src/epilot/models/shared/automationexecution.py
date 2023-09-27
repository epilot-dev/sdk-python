"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import automationaction as shared_automationaction
from ..shared import cartcheckoutaction as shared_cartcheckoutaction
from ..shared import createdocumentaction as shared_createdocumentaction
from ..shared import executionstatus as shared_executionstatus
from ..shared import mapentityaction as shared_mapentityaction
from ..shared import sendemailaction as shared_sendemailaction
from ..shared import triggerevententityactivity as shared_triggerevententityactivity
from ..shared import triggerevententityoperation as shared_triggerevententityoperation
from ..shared import triggereventmanual as shared_triggereventmanual
from ..shared import triggerwebhookaction as shared_triggerwebhookaction
from ..shared import triggerworkflowaction as shared_triggerworkflowaction
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from epilot import utils
from typing import Any, Optional, Union



@dataclasses.dataclass
class AutomationExecutionTriggerEvent:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AutomationExecution:
    actions: list[Union[shared_mapentityaction.MapEntityAction, shared_triggerworkflowaction.TriggerWorkflowAction, shared_triggerwebhookaction.TriggerWebhookAction, shared_createdocumentaction.CreateDocumentAction, shared_sendemailaction.SendEmailAction, shared_cartcheckoutaction.CartCheckoutAction, shared_automationaction.AutomationAction]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions') }})
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id') }})
    flow_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flow_id') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activity_id'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    current_action_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_action_id'), 'exclude': lambda f: f is None }})
    entity_snapshot: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_snapshot'), 'exclude': lambda f: f is None }})
    execution_status: Optional[shared_executionstatus.ExecutionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('execution_status'), 'exclude': lambda f: f is None }})
    flow_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flow_name'), 'exclude': lambda f: f is None }})
    trigger_event: Optional[Union[shared_triggereventmanual.TriggerEventManual, shared_triggerevententityactivity.TriggerEventEntityActivity, shared_triggerevententityoperation.TriggerEventEntityOperation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trigger_event'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

