"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class SendEmailConfigAttachmentsSourceFilterDocumentType(str, Enum):
    r"""Filter by a specific document type (e.g. document)"""
    DOCUMENT = 'document'
    TEXT = 'text'
    IMAGE = 'image'
    VIDEO = 'video'
    AUDIO = 'audio'
    SPREADSHEET = 'spreadsheet'
    PRESENTATION = 'presentation'
    FONT = 'font'
    ARCHIVE = 'archive'
    APPLICATION = 'application'
    UNKNOWN = 'unknown'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendEmailConfigAttachmentsSourceFilter:
    r"""Specify filters to match file entities related to main entity"""
    
    attribute: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribute'), 'exclude': lambda f: f is None }})
    r"""Filter by a specific relation attribute on the main entity"""
    document_type: Optional[SendEmailConfigAttachmentsSourceFilterDocumentType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_type'), 'exclude': lambda f: f is None }})
    r"""Filter by a specific document type (e.g. document)"""
    filename_regex: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename_regex'), 'exclude': lambda f: f is None }})
    r"""Match by filename. Regex syntax supported"""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    r"""Limit files to maximum number (default, all matched file relations)"""
    relation_tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relation_tag'), 'exclude': lambda f: f is None }})
    r"""Filter by relation tag (label) on the main entity"""
    self_: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self'), 'exclude': lambda f: f is None }})
    r"""Picks main entity as file (only works if source entity is a file)"""
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    r"""Filter by a specific tag on the related file entity"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendEmailConfigAttachments:
    
    source_filter: Optional[SendEmailConfigAttachmentsSourceFilter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_filter'), 'exclude': lambda f: f is None }})
    r"""Specify filters to match file entities related to main entity"""
    
class SendEmailConfigLanguageCode(str, Enum):
    DE = 'de'
    EN = 'en'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SendEmailConfig:
    
    attachments: Optional[list[SendEmailConfigAttachments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    r"""Include extra file attachments in sent email.
    
    Attachments in email template will be sent regardless of this configuration.
    """
    email_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_template_id'), 'exclude': lambda f: f is None }})
    language_code: Optional[SendEmailConfigLanguageCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language_code'), 'exclude': lambda f: f is None }})
    