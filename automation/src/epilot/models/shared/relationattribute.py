"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any, Optional

class RelationAttributeMode(str, Enum):
    APPEND = 'append'
    PREPEND = 'prepend'
    SET = 'set'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttributeSourceFilter:
    r"""A filter to identify which source entities to pick as relations from main entity"""
    
    attribute: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribute'), 'exclude': lambda f: f is None }})
    r"""Filter by a specific relation attribute on the main entity"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    r"""Limit relations to maximum number (default, all matched relations)"""
    relation_tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relation_tag'), 'exclude': lambda f: f is None }})
    r"""Filter by relation tag (label) on the main entity"""
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""Filter by specific schema"""
    self_: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self'), 'exclude': lambda f: f is None }})
    r"""Picks main entity as relation (overrides other filters)"""
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    r"""Filter by a specific tag on the related entity"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttribute:
    
    mode: RelationAttributeMode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode') }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target') }})
    r"""Target attribute to store the relation in"""
    related_to: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('related_to'), 'exclude': lambda f: f is None }})
    source_filter: Optional[RelationAttributeSourceFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_filter'), 'exclude': lambda f: f is None }})
    r"""A filter to identify which source entities to pick as relations from main entity"""
    target_tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_tags'), 'exclude': lambda f: f is None }})
    r"""Relation tags (labels) to set for the stored relations"""
    target_tags_include_source: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_tags_include_source'), 'exclude': lambda f: f is None }})
    r"""Include all relation tags (labels) present on the main entity relation"""
    