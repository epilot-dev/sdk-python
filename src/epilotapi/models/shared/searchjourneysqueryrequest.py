import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class SearchJourneysQueryRequest:
    from_: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('from') }})
    q: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('q') }})
    size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('size') }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sort') }})
    
