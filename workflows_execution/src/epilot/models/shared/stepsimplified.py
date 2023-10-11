"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import ecpdetails as shared_ecpdetails
from ..shared import itemtype as shared_itemtype
from ..shared import steprequirement as shared_steprequirement
from ..shared import steptype as shared_steptype
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StepSimplified:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    type: shared_itemtype.ItemType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    definition_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('definitionId'), 'exclude': lambda f: f is None }})
    ecp: Optional[shared_ecpdetails.ECPDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecp'), 'exclude': lambda f: f is None }})
    r"""Details regarding ECP for the workflow step"""
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    entity_ref_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entityRefId'), 'exclude': lambda f: f is None }})
    r"""This field is deprecated. It will be soon removed. Please use only id.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    execution_type: Optional[shared_steptype.StepType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('executionType'), 'exclude': lambda f: f is None }})
    requirements: Optional[list[shared_steprequirement.StepRequirement]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requirements'), 'exclude': lambda f: f is None }})
    

