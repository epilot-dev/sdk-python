import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

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


@dataclass_json
@dataclasses.dataclass
class SearchMappings:
    fields: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fields') }})
    index: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('index') }})
    type: Optional[SearchMappingsTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
