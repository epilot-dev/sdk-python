"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import optin as shared_optin
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SubmissionPayload:
    r"""Holds content and meta information"""
    entities: list[dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entities') }})
    r"""Entities to create from submission"""
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""organization id"""
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id') }})
    r"""identifier for source e.g. journey ID or frontend ID"""
    source_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_type') }})
    r"""type of source, e.g. journey or frontend"""
    ivy_opportunity_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_ivy_opportunity_ids'), 'exclude': lambda f: f is None }})
    r"""Related Ivy Opportunity Ids

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    journey_submit_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journey_submit_id'), 'exclude': lambda f: f is None }})
    r"""journey submit uid"""
    opt_ins: Optional[list[shared_optin.OptIn]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('opt_ins'), 'exclude': lambda f: f is None }})
    r"""Opt-ins to create from submission"""
    

