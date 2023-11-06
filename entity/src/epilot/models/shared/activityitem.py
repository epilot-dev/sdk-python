"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import activitycallercontext as shared_activitycallercontext
from ..shared import entityoperation as shared_entityoperation
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from epilot import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityItem:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""Message for activity. Supports handlebars syntax."""
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    r"""Title for activity. Supports handlebars syntax."""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id'), 'exclude': lambda f: f is None }})
    r"""See https://github.com/ulid/spec"""
    caller: Optional[shared_activitycallercontext.ActivityCallerContext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('caller'), 'exclude': lambda f: f is None }})
    operations: Optional[List[shared_entityoperation.EntityOperation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operations'), 'exclude': lambda f: f is None }})
    operations_total: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operations_total'), 'exclude': lambda f: f is None }})
    r"""Count of total operations attached to this activity"""
    payload: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload'), 'exclude': lambda f: f is None }})
    timestamp: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    

