"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any, Dict, Optional

class SearchMappingsType(str, Enum):
    KEYWORD = 'keyword'
    TEXT = 'text'
    BOOLEAN = 'boolean'
    INTEGER = 'integer'
    LONG = 'long'
    FLOAT = 'float'
    DATE = 'date'
    FLATTENED = 'flattened'
    NESTED = 'nested'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchMappings:
    fields_: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is None }})
    index: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index'), 'exclude': lambda f: f is None }})
    type: Optional[SearchMappingsType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

