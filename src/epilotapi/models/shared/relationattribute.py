import dataclasses
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

class RelationAttributeActionsActionTypeEnum(str, Enum):
    ADD_EXISTING = "add_existing"
    CREATE_NEW = "create_new"
    CREATE_FROM_EXISTING = "create_from_existing"


@dataclass_json
@dataclasses.dataclass
class RelationAttributeActions:
    action_type: Optional[RelationAttributeActionsActionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('action_type') }})
    default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default') }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    new_entity_item: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('new_entity_item') }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag') }})
    
class RelationAttributeDrawerSizeEnum(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class RelationAttributeEditModeEnum(str, Enum):
    LIST_VIEW = "list-view"

class RelationAttributeRelationAffinityModeEnum(str, Enum):
    WEAK = "weak"
    STRONG = "strong"

class RelationAttributeRelationTypeEnum(str, Enum):
    HAS_MANY = "has_many"
    HAS_ONE = "has_one"

class RelationAttributeTypeEnum(str, Enum):
    RELATION = "relation"


@dataclass_json
@dataclasses.dataclass
class RelationAttribute:
    r"""RelationAttribute
    Entity Relationship
    """
    
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_purpose') }})
    actions: Optional[list[RelationAttributeActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions') }})
    add_button_label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('add_button_label') }})
    allowed_schemas: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allowedSchemas') }})
    constraints: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('constraints') }})
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default_value') }})
    deprecated: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deprecated') }})
    details_view_mode_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details_view_mode_enabled') }})
    drawer_size: Optional[RelationAttributeDrawerSizeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('drawer_size') }})
    edit_mode: Optional[RelationAttributeEditModeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('edit_mode') }})
    enable_relation_picker: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_relation_picker') }})
    enable_relation_tags: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_relation_tags') }})
    entity_builder_disable_edit: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_builder_disable_edit') }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('group') }})
    has_primary: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('has_primary') }})
    hidden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hidden') }})
    hide_label: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hide_label') }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }})
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('layout') }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }})
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('placeholder') }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('preview_value_formatter') }})
    protected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('protected') }})
    readonly: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('readonly') }})
    relation_affinity_mode: Optional[RelationAttributeRelationAffinityModeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_affinity_mode') }})
    relation_type: Optional[RelationAttributeRelationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_type') }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    reverse_attributes: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reverse_attributes') }})
    search_placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('search_placeholder') }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag') }})
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_in_table') }})
    summary_fields: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('summary_fields') }})
    type: Optional[RelationAttributeTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value_formatter') }})
    
