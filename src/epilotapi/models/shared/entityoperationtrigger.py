import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional

class EntityOperationTriggerConfigurationOperationsEnum(str, Enum):
    CREATE_ENTITY = "createEntity"
    UPDATE_ENTITY = "updateEntity"
    DELETE_ENTITY = "deleteEntity"


@dataclass_json
@dataclasses.dataclass
class EntityOperationTriggerConfiguration:
    operations: list[EntityOperationTriggerConfigurationOperationsEnum] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('operations') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema') }})
    exclude_activities: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('exclude_activities') }})
    include_activities: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('include_activities') }})
    
class EntityOperationTriggerTypeEnum(str, Enum):
    ENTITY_OPERATION = "entity_operation"


@dataclass_json
@dataclasses.dataclass
class EntityOperationTrigger:
    configuration: EntityOperationTriggerConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('configuration') }})
    type: EntityOperationTriggerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    