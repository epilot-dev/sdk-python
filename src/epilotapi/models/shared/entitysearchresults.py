import dataclasses
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class EntitySearchResults:
    hits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hits') }})
    results: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    