import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from epilotapi import utils

class SendEmailConfigAttachmentsSourceFilterDocumentTypeEnum(str, Enum):
    DOCUMENT = "document"
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    SPREADSHEET = "spreadsheet"
    PRESENTATION = "presentation"
    FONT = "font"
    ARCHIVE = "archive"
    APPLICATION = "application"
    UNKNOWN = "unknown"


@dataclass_json
@dataclasses.dataclass
class SendEmailConfigAttachmentsSourceFilter:
    r"""SendEmailConfigAttachmentsSourceFilter
    Specify filters to match file entities related to main entity
    """
    
    attribute: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attribute') }})
    document_type: Optional[SendEmailConfigAttachmentsSourceFilterDocumentTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('document_type') }})
    filename_regex: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filename_regex') }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit') }})
    relation_tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_tag') }})
    self: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag') }})
    

@dataclass_json
@dataclasses.dataclass
class SendEmailConfigAttachments:
    source_filter: Optional[SendEmailConfigAttachmentsSourceFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_filter') }})
    
class SendEmailConfigLanguageCodeEnum(str, Enum):
    DE = "de"
    EN = "en"


@dataclass_json
@dataclasses.dataclass
class SendEmailConfig:
    attachments: Optional[list[SendEmailConfigAttachments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachments') }})
    email_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email_template_id') }})
    language_code: Optional[SendEmailConfigLanguageCodeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('language_code') }})
    
