"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .settingflag import SettingFlag, SettingFlagTypedDict
from enum import Enum
from epilot_entity.types import BaseModel
import pydantic
from typing import Any, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class NumberAttributeConstraintsTypedDict(TypedDict):
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.

    """
    
    

class NumberAttributeConstraints(BaseModel):
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.

    """
    
    

class NumberAttributeInfoHelpersTypedDict(TypedDict):
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    
    hint_custom_component: NotRequired[str]
    r"""The name of the custom component to be used as the hint helper.
    The component should be registered in the `@epilot360/entity-ui` on the index of the components directory.
    When specified it overrides the `hint_text` or `hint_text_key` configuration.

    """
    hint_text: NotRequired[str]
    r"""The text to be displayed in the attribute hint helper.
    When specified it overrides the `hint_text_key` configuration.

    """
    hint_text_key: NotRequired[str]
    r"""The key of the hint text to be displayed in the attribute hint helper.
    The key should be a valid i18n key.

    """
    hint_tooltip_placement: NotRequired[str]
    r"""The placement of the hint tooltip.
    The value should be a valid `@mui/core` tooltip placement.

    """
    

class NumberAttributeInfoHelpers(BaseModel):
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    
    hint_custom_component: Optional[str] = None
    r"""The name of the custom component to be used as the hint helper.
    The component should be registered in the `@epilot360/entity-ui` on the index of the components directory.
    When specified it overrides the `hint_text` or `hint_text_key` configuration.

    """
    hint_text: Optional[str] = None
    r"""The text to be displayed in the attribute hint helper.
    When specified it overrides the `hint_text_key` configuration.

    """
    hint_text_key: Optional[str] = None
    r"""The key of the hint text to be displayed in the attribute hint helper.
    The key should be a valid i18n key.

    """
    hint_tooltip_placement: Optional[str] = None
    r"""The placement of the hint tooltip.
    The value should be a valid `@mui/core` tooltip placement.

    """
    

class NumberAttributeType(str, Enum):
    NUMBER = "number"

class NumberAttributeTypedDict(TypedDict):
    r"""Numeric input"""
    
    label: str
    name: str
    purpose: NotRequired[List[str]]
    constraints: NotRequired[NumberAttributeConstraintsTypedDict]
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.

    """
    default_value: NotRequired[Any]
    deprecated: NotRequired[bool]
    entity_builder_disable_edit: NotRequired[bool]
    r"""Setting to `true` disables editing the attribute on the entity builder UI"""
    feature_flag: NotRequired[str]
    r"""This attribute should only be active when the feature flag is enabled"""
    format: NotRequired[str]
    group: NotRequired[str]
    r"""Which group the attribute should appear in. Accepts group ID or group name"""
    hidden: NotRequired[bool]
    r"""Do not render attribute in entity views"""
    hide_label: NotRequired[bool]
    r"""When set to true, will hide the label of the field."""
    icon: NotRequired[str]
    r"""Code name of the icon to used to represent this attribute.
    The value must be a valid @epilot/base-elements Icon name

    """
    id: NotRequired[str]
    r"""ID for the entity attribute"""
    info_helpers: NotRequired[NumberAttributeInfoHelpersTypedDict]
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    layout: NotRequired[str]
    order: NotRequired[int]
    r"""Attribute sort order (ascending) in group"""
    placeholder: NotRequired[str]
    preview_value_formatter: NotRequired[str]
    protected: NotRequired[bool]
    r"""Setting to `true` prevents the attribute from being modified / deleted"""
    readonly: NotRequired[bool]
    render_condition: NotRequired[str]
    r"""Defines the conditional rendering expression for showing this field.
    When a valid expression is parsed, their evaluation defines the visibility of this attribute.
    Note: Empty or invalid expression have no effect on the field visibility.

    """
    required: NotRequired[bool]
    settings_flag: NotRequired[List[SettingFlagTypedDict]]
    r"""This attribute should only be active when all the settings have the correct value"""
    show_in_table: NotRequired[bool]
    r"""Render as a column in table views. When defined, overrides `hidden`"""
    show_separator: NotRequired[bool]
    r"""Whether or not to show a thousands separator"""
    sortable: NotRequired[bool]
    r"""Allow sorting by this attribute in table views if `show_in_table` is true"""
    type: NotRequired[NumberAttributeType]
    value_formatter: NotRequired[str]
    

class NumberAttribute(BaseModel):
    r"""Numeric input"""
    
    label: str
    name: str
    purpose: Annotated[Optional[List[str]], pydantic.Field(alias="_purpose")] = None
    constraints: Optional[NumberAttributeConstraints] = None
    r"""A set of constraints applicable to the attribute.
    These constraints should and will be enforced by the attribute renderer.

    """
    default_value: Optional[Any] = None
    deprecated: Optional[bool] = False
    entity_builder_disable_edit: Optional[bool] = False
    r"""Setting to `true` disables editing the attribute on the entity builder UI"""
    feature_flag: Optional[str] = None
    r"""This attribute should only be active when the feature flag is enabled"""
    format: Optional[str] = None
    group: Optional[str] = None
    r"""Which group the attribute should appear in. Accepts group ID or group name"""
    hidden: Optional[bool] = False
    r"""Do not render attribute in entity views"""
    hide_label: Optional[bool] = None
    r"""When set to true, will hide the label of the field."""
    icon: Optional[str] = None
    r"""Code name of the icon to used to represent this attribute.
    The value must be a valid @epilot/base-elements Icon name

    """
    id: Optional[str] = None
    r"""ID for the entity attribute"""
    info_helpers: Optional[NumberAttributeInfoHelpers] = None
    r"""A set of configurations meant to document and assist the user in filling the attribute."""
    layout: Optional[str] = None
    order: Optional[int] = None
    r"""Attribute sort order (ascending) in group"""
    placeholder: Optional[str] = None
    preview_value_formatter: Optional[str] = None
    protected: Optional[bool] = None
    r"""Setting to `true` prevents the attribute from being modified / deleted"""
    readonly: Optional[bool] = False
    render_condition: Optional[str] = None
    r"""Defines the conditional rendering expression for showing this field.
    When a valid expression is parsed, their evaluation defines the visibility of this attribute.
    Note: Empty or invalid expression have no effect on the field visibility.

    """
    required: Optional[bool] = False
    settings_flag: Optional[List[SettingFlag]] = None
    r"""This attribute should only be active when all the settings have the correct value"""
    show_in_table: Optional[bool] = None
    r"""Render as a column in table views. When defined, overrides `hidden`"""
    show_separator: Optional[bool] = True
    r"""Whether or not to show a thousands separator"""
    sortable: Optional[bool] = True
    r"""Allow sorting by this attribute in table views if `show_in_table` is true"""
    type: Optional[NumberAttributeType] = None
    value_formatter: Optional[str] = None
    
