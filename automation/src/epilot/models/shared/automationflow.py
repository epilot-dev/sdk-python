"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import triggercondition as shared_triggercondition
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from epilot import utils
from marshmallow import fields
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AutomationFlow:
    r"""The created automation flow"""
    
    actions: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions') }})

    flow_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flow_name') }})

    r"""A descriptive name for the Automation"""
    triggers: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('triggers') }})

    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})

    created_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by'), 'exclude': lambda f: f is None }})

    r"""User / service who created automation flow"""
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})

    r"""Whether the automation is enabled or not"""
    entity_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_schema'), 'exclude': lambda f: f is None }})

    r"""The triggering entity schema"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})

    last_updated_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_updated_by'), 'exclude': lambda f: f is None }})

    r"""User / service who last updated automation flow"""
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id'), 'exclude': lambda f: f is None }})

    r"""Organization the automation flow belongs to"""
    runs: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runs'), 'exclude': lambda f: f is None }})

    r"""Number of automation executions that ran"""
    trigger_conditions: Optional[list[shared_triggercondition.TriggerCondition]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trigger_conditions'), 'exclude': lambda f: f is None }})

    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AutomationFlowInput:
    r"""Automation flow to create"""
    
    flow_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flow_name') }})

    r"""A descriptive name for the Automation"""
    triggers: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('triggers') }})

    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})

    r"""Whether the automation is enabled or not"""
    entity_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_schema'), 'exclude': lambda f: f is None }})

    r"""The triggering entity schema"""
    runs: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runs'), 'exclude': lambda f: f is None }})

    r"""Number of automation executions that ran"""
    trigger_conditions: Optional[list[shared_triggercondition.TriggerCondition]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trigger_conditions'), 'exclude': lambda f: f is None }})

    