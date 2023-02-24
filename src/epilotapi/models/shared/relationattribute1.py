from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Any, Optional

class RelationAttribute1ModeEnum(str, Enum):
    APPEND = "append"
    PREPEND = "prepend"
    SET = "set"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttribute1SourceFilter:
    r"""RelationAttribute1SourceFilter
    A filter to identify which source entities to pick as relations from main entity
    """
    
    attribute: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attribute'), 'exclude': lambda f: f is None }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit'), 'exclude': lambda f: f is None }})
    relation_tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_tag'), 'exclude': lambda f: f is None }})
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema'), 'exclude': lambda f: f is None }})
    self: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('self'), 'exclude': lambda f: f is None }})
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttribute1:
    mode: RelationAttribute1ModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('mode') }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    related_to: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('related_to'), 'exclude': lambda f: f is None }})
    source_filter: Optional[RelationAttribute1SourceFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_filter'), 'exclude': lambda f: f is None }})
    target_tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_tags'), 'exclude': lambda f: f is None }})
    target_tags_include_source: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_tags_include_source'), 'exclude': lambda f: f is None }})
    