"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import entityacl as shared_entityacl
from ..shared import entityowner as shared_entityowner
from ..shared import relationitem as shared_relationitem
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from epilot import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationEntity:
    created_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id') }})
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org') }})
    r"""Organization Id the entity belongs to"""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_schema') }})
    r"""URL-friendly identifier for the entity schema"""
    title: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title') }})
    r"""Title of entity"""
    updated_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    acl: Optional[shared_entityacl.EntityACL] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_acl'), 'exclude': lambda f: f is None }})
    r"""Access control list (ACL) for an entity. Defines sharing access to external orgs or users."""
    owners: Optional[List[shared_entityowner.EntityOwner]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_owners'), 'exclude': lambda f: f is None }})
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags') }})
    dollar_relation: Optional[shared_relationitem.RelationItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$relation'), 'exclude': lambda f: f is None }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

