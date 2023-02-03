import dataclasses
from typing import Any,Optional
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import mappingattributev2 as shared_mappingattributev2
from ..shared import setvaluemapper as shared_setvaluemapper
from ..shared import copyvaluemapper as shared_copyvaluemapper
from ..shared import appendvaluemapper as shared_appendvaluemapper
from ..shared import mappingconfigref as shared_mappingconfigref
from ..shared import relationattribute1 as shared_relationattribute1


@dataclass_json
@dataclasses.dataclass
class MapEntityConfig:
    target_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_schema') }})
    linkback_relation_attribute: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkback_relation_attribute') }})
    linkback_relation_tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkback_relation_tags') }})
    mapping_attributes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mapping_attributes') }})
    mapping_config: Optional[shared_mappingconfigref.MappingConfigRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mapping_config') }})
    relation_attributes: Optional[list[shared_relationattribute1.RelationAttribute1]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_attributes') }})
    target_unique: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_unique') }})
    
