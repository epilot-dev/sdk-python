from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Any, Optional

class SearchMappingsTypeEnum(str, Enum):
    KEYWORD = "keyword"
    TEXT = "text"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    LONG = "long"
    FLOAT = "float"
    DATE = "date"
    FLATTENED = "flattened"
    NESTED = "nested"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchMappings:
    fields: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fields'), 'exclude': lambda f: f is None }})
    index: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index'), 'exclude': lambda f: f is None }})
    type: Optional[SearchMappingsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    