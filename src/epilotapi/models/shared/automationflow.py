import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import mapentityactionconfig as shared_mapentityactionconfig
from ..shared import triggerworkflowactionconfig as shared_triggerworkflowactionconfig
from ..shared import triggerwebhookactionconfig as shared_triggerwebhookactionconfig
from ..shared import createdocumentactionconfig as shared_createdocumentactionconfig
from ..shared import sendemailactionconfig as shared_sendemailactionconfig
from ..shared import cartcheckoutactionconfig as shared_cartcheckoutactionconfig
from ..shared import automationactionconfig as shared_automationactionconfig
from ..shared import triggercondition as shared_triggercondition
from ..shared import frontendsubmittrigger as shared_frontendsubmittrigger
from ..shared import journeysubmittrigger as shared_journeysubmittrigger
from ..shared import apisubmissiontrigger as shared_apisubmissiontrigger
from ..shared import entityoperationtrigger as shared_entityoperationtrigger
from ..shared import activitytrigger as shared_activitytrigger
from ..shared import entitymanualtrigger as shared_entitymanualtrigger
from ..shared import receivedemailtrigger as shared_receivedemailtrigger


@dataclass_json
@dataclasses.dataclass
class AutomationFlow:
    actions: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions') }})
    flow_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('flow_name') }})
    triggers: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('triggers') }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    entity_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_schema') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    last_updated_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_updated_by') }})
    runs: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('runs') }})
    trigger_conditions: Optional[list[shared_triggercondition.TriggerCondition]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('trigger_conditions') }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    
