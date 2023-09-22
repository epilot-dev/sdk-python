"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Any, Optional



@dataclasses.dataclass
class MultiSelectAttributeConstraints:
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MultiSelectAttributeInfoHelpers:
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
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MultiSelectAttributeOptions2:
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    


class MultiSelectAttributeType(str, Enum):
    MULTISELECT = 'multiselect'
    CHECKBOX = 'checkbox'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MultiSelectAttribute:
    r"""Multi Choice Selection"""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_purpose'), 'exclude': lambda f: f is None }})
    allow_any: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_any'), 'exclude': lambda f: f is None }})
    r"""Allow arbitrary input values in addition to provided options"""
    allow_extra_options: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_extra_options'), 'exclude': lambda f: f is None }})
    r"""controls if the 360 ui will allow the user to enter a value which is not defined by the options"""
    constraints: Optional[MultiSelectAttributeConstraints] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('constraints'), 'exclude': lambda f: f is None }})
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.
    """
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_value'), 'exclude': lambda f: f is None }})
    deprecated: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deprecated'), 'exclude': lambda f: f is None }})
    disable_case_sensitive: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disable_case_sensitive'), 'exclude': lambda f: f is None }})
    r"""controls if the matching of values against the options is case sensitive or not"""
    entity_builder_disable_edit: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_builder_disable_edit'), 'exclude': lambda f: f is None }})
    r"""Setting to `true` disables editing the attribute on the entity builder UI"""
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag'), 'exclude': lambda f: f is None }})
    r"""This attribute should only be active when the feature flag is enabled"""
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    r"""Which group the attribute should appear in. Accepts group ID or group name"""
    hidden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hidden'), 'exclude': lambda f: f is None }})
    r"""Do not render attribute in entity views"""
    hide_label: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hide_label'), 'exclude': lambda f: f is None }})
    r"""When set to true, will hide the label of the field."""
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    r"""Code name of the icon to used to represent this attribute.
    The value must be a valid @epilot/base-elements Icon name
    """
    info_helpers: Optional[MultiSelectAttributeInfoHelpers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('info_helpers'), 'exclude': lambda f: f is None }})
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('layout'), 'exclude': lambda f: f is None }})
    options: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    r"""Attribute sort order (ascending) in group"""
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('placeholder'), 'exclude': lambda f: f is None }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preview_value_formatter'), 'exclude': lambda f: f is None }})
    protected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protected'), 'exclude': lambda f: f is None }})
    r"""Setting to `true` prevents the attribute from being modified / deleted"""
    readonly: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('readonly'), 'exclude': lambda f: f is None }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('render_condition'), 'exclude': lambda f: f is None }})
    r"""Defines the conditional rendering expression for showing this field.
    When a valid expression is parsed, their evaluation defines the visibility of this attribute.
    Note: Empty or invalid expression have no effect on the field visibility.
    """
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setting_flag'), 'exclude': lambda f: f is None }})
    r"""This attribute should only be active when the setting is enabled"""
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_in_table'), 'exclude': lambda f: f is None }})
    r"""Render as a column in table views. When defined, overrides `hidden`"""
    sortable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sortable'), 'exclude': lambda f: f is None }})
    r"""Allow sorting by this attribute in table views if `show_in_table` is true"""
    type: Optional[MultiSelectAttributeType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value_formatter'), 'exclude': lambda f: f is None }})
    

