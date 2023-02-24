from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilotapi import utils
from typing import Optional

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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendEmailConfigAttachmentsSourceFilter:
    r"""SendEmailConfigAttachmentsSourceFilter
    Specify filters to match file entities related to main entity
    """
    
    attribute: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attribute'), 'exclude': lambda f: f is None }})
    document_type: Optional[SendEmailConfigAttachmentsSourceFilterDocumentTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('document_type'), 'exclude': lambda f: f is None }})
    filename_regex: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filename_regex'), 'exclude': lambda f: f is None }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('limit'), 'exclude': lambda f: f is None }})
    relation_tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relation_tag'), 'exclude': lambda f: f is None }})
    self: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('self'), 'exclude': lambda f: f is None }})
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendEmailConfigAttachments:
    source_filter: Optional[SendEmailConfigAttachmentsSourceFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_filter'), 'exclude': lambda f: f is None }})
    
class SendEmailConfigLanguageCodeEnum(str, Enum):
    DE = "de"
    EN = "en"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendEmailConfig:
    attachments: Optional[list[SendEmailConfigAttachments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachments'), 'exclude': lambda f: f is None }})
    email_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('email_template_id'), 'exclude': lambda f: f is None }})
    language_code: Optional[SendEmailConfigLanguageCodeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('language_code'), 'exclude': lambda f: f is None }})
    