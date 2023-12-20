"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any, List, Optional


@dataclasses.dataclass
class RepeatableAttributeConstraints:
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RepeatableAttributeInfoHelpers:
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
    


class RepeatableAttributeRelationAffinityMode(str, Enum):
    r"""Weak repeatable attributes are kept when duplicating an entity. Strong repeatable attributes are discarded when duplicating an entity."""
    WEAK = 'weak'
    STRONG = 'strong'

class RepeatableAttributeType(str, Enum):
    STRING = 'string'
    PHONE = 'phone'
    EMAIL = 'email'
    ADDRESS = 'address'
    RELATION = 'relation'
    PAYMENT = 'payment'
    PRICE_COMPONENT = 'price_component'
    DATE = 'date'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RepeatableAttribute:
    r"""Repeatable (add N number of fields)"""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    purpose: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_purpose'), 'exclude': lambda f: f is None }})
    constraints: Optional[RepeatableAttributeConstraints] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('constraints'), 'exclude': lambda f: f is None }})
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.
    """
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_value'), 'exclude': lambda f: f is None }})
    deprecated: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deprecated'), 'exclude': lambda f: f is None }})
    enable_relation_picker: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_relation_picker'), 'exclude': lambda f: f is None }})
    r"""when enable_relation_picker is set to true the user will be able to pick existing relations as values. Otherwise, the user will need to create new relation to link."""
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
    r"""Code name of the icon to used to represent this attribute.
    The value must be a valid @epilot/base-elements Icon name
    """
    info_helpers: Optional[RepeatableAttributeInfoHelpers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('info_helpers'), 'exclude': lambda f: f is None }})
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('layout'), 'exclude': lambda f: f is None }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    r"""Attribute sort order (ascending) in group"""
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('placeholder'), 'exclude': lambda f: f is None }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preview_value_formatter'), 'exclude': lambda f: f is None }})
    protected: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protected'), 'exclude': lambda f: f is None }})
    r"""Setting to `true` prevents the attribute from being modified / deleted"""
    readonly: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('readonly'), 'exclude': lambda f: f is None }})
    relation_affinity_mode: Optional[RepeatableAttributeRelationAffinityMode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relation_affinity_mode'), 'exclude': lambda f: f is None }})
    r"""Weak repeatable attributes are kept when duplicating an entity. Strong repeatable attributes are discarded when duplicating an entity."""
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('render_condition'), 'exclude': lambda f: f is None }})
    r"""Defines the conditional rendering expression for showing this field.
    When a valid expression is parsed, their evaluation defines the visibility of this attribute.
    Note: Empty or invalid expression have no effect on the field visibility.
    """
    repeatable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('repeatable'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setting_flag'), 'exclude': lambda f: f is None }})
    r"""This attribute should only be active when the setting is enabled"""
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_in_table'), 'exclude': lambda f: f is None }})
    r"""Render as a column in table views. When defined, overrides `hidden`"""
    sortable: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortable'), 'exclude': lambda f: f is None }})
    r"""Allow sorting by this attribute in table views if `show_in_table` is true"""
    type: Optional[RepeatableAttributeType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value_formatter'), 'exclude': lambda f: f is None }})
    

