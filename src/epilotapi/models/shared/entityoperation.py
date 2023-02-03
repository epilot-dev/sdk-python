import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class EntityOperationDiff:
    added: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('added') }})
    deleted: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }})
    updated: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated') }})
    
class EntityOperationOperationEnum(str, Enum):
    CREATE_ENTITY = "createEntity"
    UPDATE_ENTITY = "updateEntity"
    DELETE_ENTITY = "deleteEntity"


@dataclass_json
@dataclasses.dataclass
class EntityOperationParams:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    

@dataclass_json
@dataclasses.dataclass
class EntityOperation:
    entity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity') }})
    operation: EntityOperationOperationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('operation') }})
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('org') }})
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('activity_id') }})
    diff: Optional[EntityOperationDiff] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('diff') }})
    params: Optional[EntityOperationParams] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('params') }})
    payload: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payload') }})
    
