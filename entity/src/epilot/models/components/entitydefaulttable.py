"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .entityaction import EntityAction
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import List, Optional, Union

class EntityDefaultTableSchemasType(str, Enum):
    LINK = 'link'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Two:
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag'), 'exclude': lambda f: f is None }})
    r"""This dropdown item should only be active when the feature flag is enabled"""
    legacy: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legacy'), 'exclude': lambda f: f is None }})
    r"""Only show item for legacy tenants (ivy)"""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    type: Optional[EntityDefaultTableSchemasType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uri'), 'exclude': lambda f: f is None }})
    


class EntityDefaultTableType(str, Enum):
    ENTITY = 'entity'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultTable1:
    entity: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity'), 'exclude': lambda f: f is None }})
    r"""URL-friendly identifier for the entity schema"""
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag'), 'exclude': lambda f: f is None }})
    r"""This dropdown item should only be active when the feature flag is enabled"""
    legacy: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legacy'), 'exclude': lambda f: f is None }})
    r"""Only show item for legacy tenants (ivy)"""
    type: Optional[EntityDefaultTableType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class DropdownItems:
    pass


@dataclasses.dataclass
class EntityDefaultTableParams:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultTableOptions:
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    params: Optional[EntityDefaultTableParams] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NavbarActions:
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    options: Optional[List[EntityDefaultTableOptions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class RowActions:
    pass

class EntityDefaultTableViewType(str, Enum):
    DEFAULT = 'default'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityDefaultTable:
    dropdown_items: Optional[List[Union[EntityDefaultTable1, Two]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dropdown_items'), 'exclude': lambda f: f is None }})
    enable_thumbnails: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_thumbnails'), 'exclude': lambda f: f is None }})
    r"""Enable the thumbnail column"""
    navbar_actions: Optional[List[NavbarActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('navbar_actions'), 'exclude': lambda f: f is None }})
    row_actions: Optional[List[Union[str, EntityAction]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('row_actions'), 'exclude': lambda f: f is None }})
    view_type: Optional[EntityDefaultTableViewType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_type'), 'exclude': lambda f: f is None }})
    

