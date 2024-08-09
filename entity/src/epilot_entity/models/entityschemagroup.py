"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .settingflag import SettingFlag, SettingFlagTypedDict
from epilot_entity.types import BaseModel
import pydantic
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class InfoTooltipTitleTypedDict(TypedDict):
    default: NotRequired[str]
    r"""Default string for info tooltip"""
    key: NotRequired[str]
    r"""Translation key for info tooltip"""
    

class InfoTooltipTitle(BaseModel):
    default: Optional[str] = None
    r"""Default string for info tooltip"""
    key: Optional[str] = None
    r"""Translation key for info tooltip"""
    

class EntitySchemaGroupTypedDict(TypedDict):
    id: str
    label: str
    purpose: NotRequired[List[str]]
    r"""Only render group when one of the purposes is enabled"""
    expanded: NotRequired[bool]
    r"""Expanded by default"""
    feature_flag: NotRequired[str]
    r"""This group should only be active when the feature flag is enabled"""
    info_tooltip_title: NotRequired[InfoTooltipTitleTypedDict]
    order: NotRequired[int]
    r"""Render order of the group"""
    render_condition: NotRequired[str]
    r"""Only render group when render_condition resolves to true"""
    settings_flag: NotRequired[List[SettingFlagTypedDict]]
    r"""This group should only be active when all the settings have the correct value"""
    

class EntitySchemaGroup(BaseModel):
    id: str
    label: str
    purpose: Annotated[Optional[List[str]], pydantic.Field(alias="_purpose")] = None
    r"""Only render group when one of the purposes is enabled"""
    expanded: Optional[bool] = False
    r"""Expanded by default"""
    feature_flag: Optional[str] = None
    r"""This group should only be active when the feature flag is enabled"""
    info_tooltip_title: Optional[InfoTooltipTitle] = None
    order: Optional[int] = 0
    r"""Render order of the group"""
    render_condition: Optional[str] = None
    r"""Only render group when render_condition resolves to true"""
    settings_flag: Optional[List[SettingFlag]] = None
    r"""This group should only be active when all the settings have the correct value"""
    
