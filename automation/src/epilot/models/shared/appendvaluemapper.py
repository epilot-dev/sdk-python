"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import mappingattributemode_enum as shared_mappingattributemode_enum
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppendValueMapper:
    
    mode: shared_mappingattributemode_enum.MappingAttributeModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})

    r"""- copy_if_exists - it replaces the target attribute with the source value - append_if_exists - it currently replaces target attribute with array like values. Useful when you have multiple values to be added into one attribute. - set_value - it sets a value to a predefined value. Must be used together with value property."""
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target') }})

    r"""JSON like target path for the attribute. Eg. last_name"""
    value_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value_json') }})

    r"""To be provided only when mapping json objects into a target attribute. Eg array of addresses."""
    source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})

    r"""JSON source path for the value to be extracted from the main entity. Eg: steps[1].['Product Info'].price"""
    target_unique: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_unique'), 'exclude': lambda f: f is None }})

    r"""Array of keys which should be used when checking for uniqueness. Eg: [country, city, postal_code]"""
    