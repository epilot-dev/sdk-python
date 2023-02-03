import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class CreateDocumentConfig:
    filename: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filename') }})
    template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('template_id') }})
    
