"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import s3reference as shared_s3reference
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class FileEntityAccessControl(str, Enum):
    PRIVATE = 'private'
    PUBLIC_READ = 'public-read'

class FileEntityType(str, Enum):
    r"""Human readable type for file"""
    DOCUMENT = 'document'
    DOCUMENT_TEMPLATE = 'document_template'
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
class FileEntityVersions:
    s3ref: Optional[shared_s3reference.S3Reference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FileEntity:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id'), 'exclude': lambda f: f is None }})
    access_control: Optional[FileEntityAccessControl] = dataclasses.field(default=FileEntityAccessControl.PRIVATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_control'), 'exclude': lambda f: f is None }})
    filename: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename'), 'exclude': lambda f: f is None }})
    mime_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mime_type'), 'exclude': lambda f: f is None }})
    r"""MIME type of the file"""
    public_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public_url'), 'exclude': lambda f: f is None }})
    r"""Direct URL for file (public only if file access control is public-read)"""
    size_bytes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('size_bytes'), 'exclude': lambda f: f is None }})
    r"""File size in bytes"""
    type: Optional[FileEntityType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Human readable type for file"""
    versions: Optional[list[FileEntityVersions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('versions'), 'exclude': lambda f: f is None }})
    

