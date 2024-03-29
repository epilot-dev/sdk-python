"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import message as shared_message
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from epilot import utils
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchThreads200ApplicationJSONResults:
    r"""Thread properties depend on API caller as it's not pre-defined. We do recommend having at least `topic` property for categorizing."""
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Created date"""  
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id') }})
    r"""Entity ID"""  
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org') }})
    r"""Ivy Organization ID the entity belongs to"""  
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_schema') }})
    r"""URL-friendly identifier for the entity schema"""  
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title') }})
    r"""Entity title"""  
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Updated date"""  
    topic: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('topic') }})
    r"""Message topic (e.g. which service sends the message or message category)"""  
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    r"""Entity tags"""  
    assigned_to: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assigned_to'), 'exclude': lambda f: f is None }})
    r"""Ivy User ID of who the message is assigned to. Default is the user who sends message."""  
    latest_message: Optional[shared_message.Message] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latest_message'), 'exclude': lambda f: f is None }})  
    latest_trash_message: Optional[shared_message.Message] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latest_trash_message'), 'exclude': lambda f: f is None }})  
    org_read_message: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_read_message'), 'exclude': lambda f: f is None }})
    r"""Ivy Organization ID of organization read the message."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchThreads200ApplicationJSON:
    r"""Success"""
    
    hits: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hits') }})
    r"""Total of matched threads"""  
    results: list[SearchThreads200ApplicationJSONResults] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    r"""Matched threads"""  
    

@dataclasses.dataclass
class SearchThreadsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    search_threads_200_application_json_object: Optional[SearchThreads200ApplicationJSON] = dataclasses.field(default=None)
    r"""Success"""  
    