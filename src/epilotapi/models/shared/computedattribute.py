import dataclasses
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

class ComputedAttributeTypeEnum(str, Enum):
    COMPUTED = "computed"


@dataclass_json
@dataclasses.dataclass
class ComputedAttribute:
    r"""ComputedAttribute
    An attribute that is computed from the entity data. For more details on how to use them, check the docs [here](https://e-pilot.atlassian.net/wiki/spaces/EO/pages/5642977476/How+To+Computed+Schema+Attributes)
    """
    
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_purpose') }})
    constraints: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('constraints') }})
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default_value') }})
    deprecated: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deprecated') }})
    entity_builder_disable_edit: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_builder_disable_edit') }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('group') }})
    hidden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hidden') }})
    hide_label: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hide_label') }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }})
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('layout') }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }})
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('placeholder') }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('preview_value_formatter') }})
    protected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('protected') }})
    readonly: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('readonly') }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag') }})
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_in_table') }})
    type: Optional[ComputedAttributeTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value_formatter') }})
    
