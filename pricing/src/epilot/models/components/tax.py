"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilot import utils
from typing import Any, Dict, List, Optional


class Behavior(str, Enum):
    EXCLUSIVE_MIXED = 'Exclusive'
    INCLUSIVE_MIXED = 'Inclusive'
    EXCLUSIVE_LOWER = 'exclusive'
    INCLUSIVE_LOWER = 'inclusive'


class TaxType(str, Enum):
    VAT = 'VAT'
    GST = 'GST'
    CUSTOM = 'Custom'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Tax:
    r"""the tax configuration"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id') }})
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org') }})
    r"""Organization Id the entity belongs to"""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_schema') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title') }})
    r"""Title of entity"""
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    behavior: Behavior = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('behavior') }})
    rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rate') }})
    type: TaxType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    region: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    region_label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region_label'), 'exclude': lambda f: f is None }})
    

