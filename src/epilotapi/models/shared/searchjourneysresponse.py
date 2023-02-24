from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilotapi import utils
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchJourneysResponseResultsCreatedBy:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    
class SearchJourneysResponseResultsJourneyVersionEnum(str, Enum):
    FLEX = "Flex"
    WIDGET = "Widget"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchJourneysResponseResults:
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_id'), 'exclude': lambda f: f is None }})
    org: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_org'), 'exclude': lambda f: f is None }})
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_schema'), 'exclude': lambda f: f is None }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_tags'), 'exclude': lambda f: f is None }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_title'), 'exclude': lambda f: f is None }})
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    created_by: Optional[list[SearchJourneysResponseResultsCreatedBy]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by'), 'exclude': lambda f: f is None }})
    design: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('design'), 'exclude': lambda f: f is None }})
    journey_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('journey_id'), 'exclude': lambda f: f is None }})
    journey_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('journey_name'), 'exclude': lambda f: f is None }})
    journey_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('journey_type'), 'exclude': lambda f: f is None }})
    journey_version: Optional[SearchJourneysResponseResultsJourneyVersionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('journey_version'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchJourneysResponse:
    hits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hits'), 'exclude': lambda f: f is None }})
    results: Optional[list[SearchJourneysResponseResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    