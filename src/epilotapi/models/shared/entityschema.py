from __future__ import annotations
import dataclasses
from ..shared import entitycapability as shared_entitycapability
from ..shared import searchmappings as shared_searchmappings
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchemaGroupSettingsInfoTooltipTitle:
    default: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default'), 'exclude': lambda f: f is None }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('key'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchemaGroupSettings:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_purpose'), 'exclude': lambda f: f is None }})
    expanded: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expanded'), 'exclude': lambda f: f is None }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag'), 'exclude': lambda f: f is None }})
    info_tooltip_title: Optional[EntitySchemaGroupSettingsInfoTooltipTitle] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('info_tooltip_title'), 'exclude': lambda f: f is None }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order'), 'exclude': lambda f: f is None }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchemaUIConfigListItem:
    summary_attributes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('summary_attributes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchemaUIConfigSharing:
    show_sharing_button: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_sharing_button'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchemaUIConfig:
    create_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('create_view'), 'exclude': lambda f: f is None }})
    edit_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('edit_view'), 'exclude': lambda f: f is None }})
    list_item: Optional[EntitySchemaUIConfigListItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('list_item'), 'exclude': lambda f: f is None }})
    sharing: Optional[EntitySchemaUIConfigSharing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sharing'), 'exclude': lambda f: f is None }})
    single_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('single_view'), 'exclude': lambda f: f is None }})
    table_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_view'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchema:
    r"""EntitySchema
    The \"type\" of an Entity. Describes the shape. Includes Entity Attributes, Relations and Capabilities.
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    plural: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plural') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    attributes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    blueprint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('blueprint'), 'exclude': lambda f: f is None }})
    capabilities: Optional[list[shared_entitycapability.EntityCapability]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('capabilities'), 'exclude': lambda f: f is None }})
    dialog_config: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dialog_config'), 'exclude': lambda f: f is None }})
    draft: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('draft'), 'exclude': lambda f: f is None }})
    enable_setting: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_setting'), 'exclude': lambda f: f is None }})
    explicit_search_mappings: Optional[dict[str, shared_searchmappings.SearchMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('explicit_search_mappings'), 'exclude': lambda f: f is None }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag'), 'exclude': lambda f: f is None }})
    group_settings: Optional[list[EntitySchemaGroupSettings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('group_settings'), 'exclude': lambda f: f is None }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon'), 'exclude': lambda f: f is None }})
    layout_settings: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('layout_settings'), 'exclude': lambda f: f is None }})
    published: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('published'), 'exclude': lambda f: f is None }})
    title_template: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('title_template'), 'exclude': lambda f: f is None }})
    ui_config: Optional[EntitySchemaUIConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ui_config'), 'exclude': lambda f: f is None }})
    version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('version'), 'exclude': lambda f: f is None }})
    