from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Any, Optional

class TagsAttributeTypeEnum(str, Enum):
    TAGS = "tags"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TagsAttribute:
    r"""TagsAttribute
    Tags
    """
    
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_purpose'), 'exclude': lambda f: f is None }})
    constraints: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('constraints'), 'exclude': lambda f: f is None }})
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default_value'), 'exclude': lambda f: f is None }})
    deprecated: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deprecated'), 'exclude': lambda f: f is None }})
    entity_builder_disable_edit: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_builder_disable_edit'), 'exclude': lambda f: f is None }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag'), 'exclude': lambda f: f is None }})
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('group'), 'exclude': lambda f: f is None }})
    hidden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hidden'), 'exclude': lambda f: f is None }})
    hide_label: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hide_label'), 'exclude': lambda f: f is None }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon'), 'exclude': lambda f: f is None }})
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('layout'), 'exclude': lambda f: f is None }})
    options: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('options'), 'exclude': lambda f: f is None }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order'), 'exclude': lambda f: f is None }})
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('placeholder'), 'exclude': lambda f: f is None }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('preview_value_formatter'), 'exclude': lambda f: f is None }})
    protected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('protected'), 'exclude': lambda f: f is None }})
    readonly: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('readonly'), 'exclude': lambda f: f is None }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition'), 'exclude': lambda f: f is None }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag'), 'exclude': lambda f: f is None }})
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_in_table'), 'exclude': lambda f: f is None }})
    suggestions: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('suggestions'), 'exclude': lambda f: f is None }})
    type: Optional[TagsAttributeTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value_formatter'), 'exclude': lambda f: f is None }})
    