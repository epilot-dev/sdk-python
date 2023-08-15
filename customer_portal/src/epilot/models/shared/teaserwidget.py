"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import widgetaction as shared_widgetaction
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeaserWidgetHeadline:
    de: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('de'), 'exclude': lambda f: f is None }})
    en: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('en'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeaserWidgetLeft:
    show: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show'), 'exclude': lambda f: f is None }})
    show_button: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('showButton'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeaserWidgetRight:
    show: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show'), 'exclude': lambda f: f is None }})
    show_button: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('showButton'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeaserWidgetSubHeadline:
    de: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('de'), 'exclude': lambda f: f is None }})
    en: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('en'), 'exclude': lambda f: f is None }})
    


class TeaserWidgetType(str, Enum):
    ACTION_WIDGET = 'ACTION_WIDGET'
    CONTENT_WIDGET = 'CONTENT_WIDGET'
    ENTITY_WIDGET = 'ENTITY_WIDGET'
    TEASER_WIDGET = 'TEASER_WIDGET'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeaserWidget:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    list_index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('listIndex') }})
    r"""Index of the widget in the list, used for ordering (left or right)"""
    type: TeaserWidgetType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    actions: Optional[list[shared_widgetaction.WidgetAction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions'), 'exclude': lambda f: f is None }})
    headline: Optional[TeaserWidgetHeadline] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headline'), 'exclude': lambda f: f is None }})
    left: Optional[TeaserWidgetLeft] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('left'), 'exclude': lambda f: f is None }})
    right: Optional[TeaserWidgetRight] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('right'), 'exclude': lambda f: f is None }})
    sub_headline: Optional[TeaserWidgetSubHeadline] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subHeadline'), 'exclude': lambda f: f is None }})
    
