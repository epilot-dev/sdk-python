"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .entityacl import EntityACL
from .entityowner import EntityOwner
from .summaryfield import SummaryField
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from epilot import utils
from typing import Any, Dict, List, Optional, Union

class ActionType(str, Enum):
    r"""The action type. Currently supported actions:

    | action | description |
    |--------|-------------|
    | add_existing | Enables the user to pick an existing entity to link as relation |
    | create_new | Enables the user to create a new entity using the first/main `allowed_schemas` schema
    | create_from_existing | Enables the user to pick an existing entity to clone from, while creating a blank new entity to link as relation |
    """
    ADD_EXISTING = 'add_existing'
    CREATE_NEW = 'create_new'
    CREATE_FROM_EXISTING = 'create_from_existing'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewEntityItem:
    created_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id') }})
    org: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org') }})
    r"""Organization Id the entity belongs to"""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_schema') }})
    r"""URL-friendly identifier for the entity schema"""
    title: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_title') }})
    r"""Title of entity"""
    updated_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    acl: Optional[EntityACL] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_acl'), 'exclude': lambda f: f is None }})
    r"""Access control list (ACL) for an entity. Defines sharing access to external orgs or users."""
    owners: Optional[List[EntityOwner]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_owners'), 'exclude': lambda f: f is None }})
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags') }})
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Actions:
    action_type: Optional[ActionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_type'), 'exclude': lambda f: f is None }})
    r"""The action type. Currently supported actions:

    | action | description |
    |--------|-------------|
    | add_existing | Enables the user to pick an existing entity to link as relation |
    | create_new | Enables the user to create a new entity using the first/main `allowed_schemas` schema
    | create_from_existing | Enables the user to pick an existing entity to clone from, while creating a blank new entity to link as relation |
    """
    default: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default'), 'exclude': lambda f: f is None }})
    r"""Sets the action as the default action, visible as the main action button."""
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag'), 'exclude': lambda f: f is None }})
    r"""Name of the feature flag that enables this action"""
    label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label'), 'exclude': lambda f: f is None }})
    r"""The action label or action translation key (i18n)"""
    new_entity_item: Optional[NewEntityItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_entity_item'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setting_flag'), 'exclude': lambda f: f is None }})
    r"""Name of the setting flag that enables this action"""
    



@dataclasses.dataclass
class RelationAttributeConstraints:
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.
    """
    


class DrawerSize(str, Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

class EditMode(str, Enum):
    LIST_VIEW = 'list-view'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttributeInfoHelpers:
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    hint_custom_component: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hint_custom_component'), 'exclude': lambda f: f is None }})
    r"""The name of the custom component to be used as the hint helper.
    The component should be registered in the `@epilot360/entity-ui` on the index of the components directory.
    When specified it overrides the `hint_text` or `hint_text_key` configuration.
    """
    hint_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hint_text'), 'exclude': lambda f: f is None }})
    r"""The text to be displayed in the attribute hint helper.
    When specified it overrides the `hint_text_key` configuration.
    """
    hint_text_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hint_text_key'), 'exclude': lambda f: f is None }})
    r"""The key of the hint text to be displayed in the attribute hint helper.
    The key should be a valid i18n key.
    """
    hint_tooltip_placement: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hint_tooltip_placement'), 'exclude': lambda f: f is None }})
    r"""The placement of the hint tooltip.
    The value should be a valid `@mui/core` tooltip placement.
    """
    


class RelationAffinityMode(str, Enum):
    r"""Weak relation attributes are kept when duplicating an entity. Strong relation attributes are discarded when duplicating an entity."""
    WEAK = 'weak'
    STRONG = 'strong'

class RelationType(str, Enum):
    HAS_MANY = 'has_many'
    HAS_ONE = 'has_one'


@dataclasses.dataclass
class SummaryFields:
    pass

class RelationAttributeType(str, Enum):
    RELATION = 'relation'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RelationAttribute:
    r"""Entity Relationship"""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    purpose: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_purpose'), 'exclude': lambda f: f is None }})
    actions: Optional[List[Actions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions'), 'exclude': lambda f: f is None }})
    add_button_label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('add_button_label'), 'exclude': lambda f: f is None }})
    r"""Optional label for the add button. The translated value for add_button_lable is used, if found else the string is used as is."""
    allowed_schemas: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allowedSchemas'), 'exclude': lambda f: f is None }})
    constraints: Optional[RelationAttributeConstraints] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('constraints'), 'exclude': lambda f: f is None }})
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.
    """
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_value'), 'exclude': lambda f: f is None }})
    deprecated: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deprecated'), 'exclude': lambda f: f is None }})
    details_view_mode_enabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details_view_mode_enabled'), 'exclude': lambda f: f is None }})
    r"""Enables the preview, edition, and creation of relation items on a Master-Details view mode."""
    drawer_size: Optional[DrawerSize] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('drawer_size'), 'exclude': lambda f: f is None }})
    edit_mode: Optional[EditMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('edit_mode'), 'exclude': lambda f: f is None }})
    enable_relation_picker: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_relation_picker'), 'exclude': lambda f: f is None }})
    r"""When enable_relation_picker is set to true the user will be able to pick existing relations as values. Otherwise, the user will need to create new relation to link."""
    enable_relation_tags: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_relation_tags'), 'exclude': lambda f: f is None }})
    r"""When enable_relation_tags is set to true the user will be able to set tags(labels) in each relation item."""
    entity_builder_disable_edit: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_builder_disable_edit'), 'exclude': lambda f: f is None }})
    r"""Setting to `true` disables editing the attribute on the entity builder UI"""
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag'), 'exclude': lambda f: f is None }})
    r"""This attribute should only be active when the feature flag is enabled"""
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    r"""Which group the attribute should appear in. Accepts group ID or group name"""
    has_primary: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_primary'), 'exclude': lambda f: f is None }})
    hidden: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hidden'), 'exclude': lambda f: f is None }})
    r"""Do not render attribute in entity views"""
    hide_label: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hide_label'), 'exclude': lambda f: f is None }})
    r"""When set to true, will hide the label of the field."""
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    info_helpers: Optional[RelationAttributeInfoHelpers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('info_helpers'), 'exclude': lambda f: f is None }})
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('layout'), 'exclude': lambda f: f is None }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    r"""Attribute sort order (ascending) in group"""
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('placeholder'), 'exclude': lambda f: f is None }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preview_value_formatter'), 'exclude': lambda f: f is None }})
    protected: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protected'), 'exclude': lambda f: f is None }})
    r"""Setting to `true` prevents the attribute from being modified / deleted"""
    readonly: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('readonly'), 'exclude': lambda f: f is None }})
    relation_affinity_mode: Optional[RelationAffinityMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relation_affinity_mode'), 'exclude': lambda f: f is None }})
    r"""Weak relation attributes are kept when duplicating an entity. Strong relation attributes are discarded when duplicating an entity."""
    relation_type: Optional[RelationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relation_type'), 'exclude': lambda f: f is None }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('render_condition'), 'exclude': lambda f: f is None }})
    r"""Defines the conditional rendering expression for showing this field.
    When a valid expression is parsed, their evaluation defines the visibility of this attribute.
    Note: Empty or invalid expression have no effect on the field visibility.
    """
    required: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    reverse_attributes: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reverse_attributes'), 'exclude': lambda f: f is None }})
    r"""Map of schema slug to target relation attribute"""
    search_placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_placeholder'), 'exclude': lambda f: f is None }})
    r"""Optional placeholder text for the relation search input. The translated value for search_placeholder is used, if found else the string is used as is."""
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setting_flag'), 'exclude': lambda f: f is None }})
    r"""This attribute should only be active when the setting is enabled"""
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_in_table'), 'exclude': lambda f: f is None }})
    r"""Render as a column in table views. When defined, overrides `hidden`"""
    sortable: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortable'), 'exclude': lambda f: f is None }})
    r"""Allow sorting by this attribute in table views if `show_in_table` is true"""
    summary_fields: Optional[List[Union[str, SummaryField]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary_fields'), 'exclude': lambda f: f is None }})
    type: Optional[RelationAttributeType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value_formatter'), 'exclude': lambda f: f is None }})
    

