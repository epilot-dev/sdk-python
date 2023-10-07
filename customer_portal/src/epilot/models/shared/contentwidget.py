"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContentWidgetHeadline:
    de: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('de'), 'exclude': lambda f: f is None }})
    en: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('en'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContentWidgetSubHeadline:
    de: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('de'), 'exclude': lambda f: f is None }})
    en: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('en'), 'exclude': lambda f: f is None }})
    


class ContentWidgetType(str, Enum):
    ACTION_WIDGET = 'ACTION_WIDGET'
    CONTENT_WIDGET = 'CONTENT_WIDGET'
    ENTITY_WIDGET = 'ENTITY_WIDGET'
    TEASER_WIDGET = 'TEASER_WIDGET'
    DOCUMENT_WIDGET = 'DOCUMENT_WIDGET'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ContentWidget:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    list_index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('listIndex') }})
    r"""Index of the widget in the list, used for ordering (left or right)"""
    type: ContentWidgetType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})
    headline: Optional[ContentWidgetHeadline] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headline'), 'exclude': lambda f: f is None }})
    sub_headline: Optional[ContentWidgetSubHeadline] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subHeadline'), 'exclude': lambda f: f is None }})
    
