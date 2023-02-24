from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationDiff:
    added: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('added'), 'exclude': lambda f: f is None }})
    deleted: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }})
    updated: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated'), 'exclude': lambda f: f is None }})
    
class EntityOperationOperationEnum(str, Enum):
    CREATE_ENTITY = "createEntity"
    UPDATE_ENTITY = "updateEntity"
    DELETE_ENTITY = "deleteEntity"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationParams:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperation:
    entity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity') }})
    operation: EntityOperationOperationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('operation') }})
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('org') }})
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('activity_id'), 'exclude': lambda f: f is None }})
    diff: Optional[EntityOperationDiff] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('diff'), 'exclude': lambda f: f is None }})
    params: Optional[EntityOperationParams] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('params'), 'exclude': lambda f: f is None }})
    payload: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('payload'), 'exclude': lambda f: f is None }})
    