"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import entity as shared_entity
from ..shared import entityacl as shared_entityacl
from ..shared import entityowner as shared_entityowner
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilot import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationDiff:
    added: Optional[shared_entity.Entity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('added'), 'exclude': lambda f: f is None }})
    deleted: Optional[shared_entity.Entity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted'), 'exclude': lambda f: f is None }})
    updated: Optional[shared_entity.Entity] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated'), 'exclude': lambda f: f is None }})
    


class EntityOperationOperation(str, Enum):
    CREATE_ENTITY = 'createEntity'
    UPDATE_ENTITY = 'updateEntity'
    DELETE_ENTITY = 'deleteEntity'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationParams:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug'), 'exclude': lambda f: f is None }})
    r"""URL-friendly identifier for the entity schema"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperationPayload:
    acl: Optional[shared_entityacl.EntityACL] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_acl'), 'exclude': lambda f: f is None }})
    r"""Access control list (ACL) for an entity. Defines sharing access to external orgs or users."""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id'), 'exclude': lambda f: f is None }})
    org: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org'), 'exclude': lambda f: f is None }})
    r"""Organization Id the entity belongs to"""
    owners: Optional[List[shared_entityowner.EntityOwner]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_owners'), 'exclude': lambda f: f is None }})
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_schema'), 'exclude': lambda f: f is None }})
    r"""URL-friendly identifier for the entity schema"""
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags') }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title') }})
    r"""Title of entity"""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityOperation:
    entity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity') }})
    operation: EntityOperationOperation = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operation') }})
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org') }})
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activity_id'), 'exclude': lambda f: f is None }})
    r"""See https://github.com/ulid/spec"""
    diff: Optional[EntityOperationDiff] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('diff'), 'exclude': lambda f: f is None }})
    params: Optional[EntityOperationParams] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params'), 'exclude': lambda f: f is None }})
    payload: Optional[EntityOperationPayload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload'), 'exclude': lambda f: f is None }})
    

