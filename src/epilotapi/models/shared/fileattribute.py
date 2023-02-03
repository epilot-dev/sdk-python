import dataclasses
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

class FileAttributeDefaultAccessControlEnum(str, Enum):
    PUBLIC_READ = "public-read"
    PRIVATE = "private"

class FileAttributeTypeEnum(str, Enum):
    IMAGE = "image"
    FILE = "file"


@dataclass_json
@dataclasses.dataclass
class FileAttribute:
    r"""FileAttribute
    File or Image Attachment
    """
    
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    type: FileAttributeTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_purpose') }})
    allowed_extensions: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allowed_extensions') }})
    constraints: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('constraints') }})
    default_access_control: Optional[FileAttributeDefaultAccessControlEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default_access_control') }})
    default_value: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default_value') }})
    deprecated: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deprecated') }})
    display_images_landscaped: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_images_landscaped') }})
    enable_description: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_description') }})
    entity_builder_disable_edit: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity_builder_disable_edit') }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('group') }})
    hidden: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hidden') }})
    hide_label: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hide_label') }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }})
    layout: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('layout') }})
    multiple: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('multiple') }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }})
    placeholder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('placeholder') }})
    preview_value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('preview_value_formatter') }})
    protected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('protected') }})
    readonly: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('readonly') }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition') }})
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('required') }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag') }})
    show_in_table: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_in_table') }})
    value_formatter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('value_formatter') }})
    
