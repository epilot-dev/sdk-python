from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Any, Optional

class RelationAttributeActionsActionTypeEnum(str, Enum):
    ADD_EXISTING = "add_existing"
    CREATE_NEW = "create_new"
    CREATE_FROM_EXISTING = "create_from_existing"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttributeActions:
    action_type: Optional[RelationAttributeActionsActionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('action_type'), 'exclude': lambda f: f is None }})
    default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default'), 'exclude': lambda f: f is None }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag'), 'exclude': lambda f: f is None }})
    label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('label'), 'exclude': lambda f: f is None }})
    new_entity_item: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('new_entity_item'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag'), 'exclude': lambda f: f is None }})
    
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttribute:
    r"""RelationAttribute
    Entity Relationship
    """
    
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_purpose'), 'exclude': lambda f: f is None }})
    actions: Optional[list[RelationAttributeActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions'), 'exclude': lambda f: f is None }})
    add_button_label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('add_button_label'), 'exclude': lambda f: f is None }})
    allowed_schemas: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allowedSchemas'), 'exclude': lambda f: f is None }})
    constraints: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('constraints'), 'exclude': lambda f: f is None }})
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default_value'), 'exclude': lambda f: f is None }})
    deprecated: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deprecated'), 'exclude': lambda f: f is None }})
    details_view_mode_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('details_view_mode_enabled'), 'exclude': lambda f: f is None }})
    drawer_size: Optional[RelationAttributeDrawerSizeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('drawer_size'), 'exclude': lambda f: f is None }})
    edit_mode: Optional[RelationAttributeEditModeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('edit_mode'), 'exclude': lambda f: f is None }})
    enable_relation_picker: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_relation_picker'), 'exclude': lambda f: f is None }})
    enable_relation_tags: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_relation_tags'), 'exclude': lambda f: f is None }})
    entity_builder_disable_edit: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_builder_disable_edit'), 'exclude': lambda f: f is None }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag'), 'exclude': lambda f: f is None }})
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('group'), 'exclude': lambda f: f is None }})
    has_primary: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('has_primary'), 'exclude': lambda f: f is None }})
    hidden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hidden'), 'exclude': lambda f: f is None }})
    hide_label: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hide_label'), 'exclude': lambda f: f is None }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon'), 'exclude': lambda f: f is None }})
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('layout'), 'exclude': lambda f: f is None }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order'), 'exclude': lambda f: f is None }})
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('placeholder'), 'exclude': lambda f: f is None }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('preview_value_formatter'), 'exclude': lambda f: f is None }})
    protected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('protected'), 'exclude': lambda f: f is None }})
    readonly: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('readonly'), 'exclude': lambda f: f is None }})
    relation_affinity_mode: Optional[RelationAttributeRelationAffinityModeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_affinity_mode'), 'exclude': lambda f: f is None }})
    relation_type: Optional[RelationAttributeRelationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_type'), 'exclude': lambda f: f is None }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    reverse_attributes: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reverse_attributes'), 'exclude': lambda f: f is None }})
    search_placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('search_placeholder'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag'), 'exclude': lambda f: f is None }})
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_in_table'), 'exclude': lambda f: f is None }})
    summary_fields: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('summary_fields'), 'exclude': lambda f: f is None }})
    type: Optional[RelationAttributeTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value_formatter'), 'exclude': lambda f: f is None }})
    