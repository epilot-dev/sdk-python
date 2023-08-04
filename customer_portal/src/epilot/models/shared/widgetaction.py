"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WidgetActionLabel:
    de: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('de'), 'exclude': lambda f: f is None }})
    en: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('en'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WidgetAction:
    label: WidgetActionLabel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    

