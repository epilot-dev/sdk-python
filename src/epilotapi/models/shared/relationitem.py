import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class RelationItem:
    attribute: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('attribute') }})
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_id') }})
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_tags') }})
    reverse: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reverse') }})
    
