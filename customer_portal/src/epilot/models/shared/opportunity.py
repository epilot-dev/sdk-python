"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilot import utils
from typing import Any, Dict, List, Optional

class OpportunitySchema(str, Enum):
    OPPORTUNITY = 'opportunity'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Opportunity:
    r"""The opportunity entity"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Creation timestamp of the entity"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id') }})
    r"""Entity ID"""
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org') }})
    r"""Organization ID the entity belongs to"""
    schema: OpportunitySchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_schema') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title') }})
    r"""Title of the entity"""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Last update timestamp of the entity"""
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    r"""Array of entity tags"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    

