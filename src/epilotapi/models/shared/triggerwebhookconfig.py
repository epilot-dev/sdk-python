import dataclasses
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class TriggerWebhookConfig:
    entity_sources: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_sources') }})
    target_webhook_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_webhook_id') }})
    