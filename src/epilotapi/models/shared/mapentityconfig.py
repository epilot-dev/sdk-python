from __future__ import annotations
import dataclasses
from ..shared import mappingconfigref as shared_mappingconfigref
from ..shared import relationattribute1 as shared_relationattribute1
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MapEntityConfig:
    target_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_schema') }})
    linkback_relation_attribute: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkback_relation_attribute'), 'exclude': lambda f: f is None }})
    linkback_relation_tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkback_relation_tags'), 'exclude': lambda f: f is None }})
    mapping_attributes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mapping_attributes'), 'exclude': lambda f: f is None }})
    mapping_config: Optional[shared_mappingconfigref.MappingConfigRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mapping_config'), 'exclude': lambda f: f is None }})
    relation_attributes: Optional[list[shared_relationattribute1.RelationAttribute1]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_attributes'), 'exclude': lambda f: f is None }})
    target_unique: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_unique'), 'exclude': lambda f: f is None }})
    