import dataclasses
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import mappingattributemode_enum as shared_mappingattributemode_enum


@dataclass_json
@dataclasses.dataclass
class CopyValueMapper:
    mode: shared_mappingattributemode_enum.MappingAttributeModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('mode') }})
    source: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    
