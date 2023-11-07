"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import List, Optional

class SaveEntityFileAccessControl(str, Enum):
    r"""Access control level for the file"""
    PRIVATE = 'private'
    PUBLIC_READ = 'public-read'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class S3ref:
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    r"""S3 bucket name"""
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""S3 key"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Files:
    filename: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename') }})
    r"""File name"""
    s3ref: S3ref = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref') }})
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    r"""Array of file tags"""
    access_control: Optional[SaveEntityFileAccessControl] = dataclasses.field(default=SaveEntityFileAccessControl.PRIVATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_control'), 'exclude': lambda f: f is None }})
    r"""Access control level for the file"""
    document_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_type'), 'exclude': lambda f: f is None }})
    r"""Document type"""
    file_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_entity_id'), 'exclude': lambda f: f is None }})
    r"""File entity ID"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SaveEntityFile:
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id') }})
    r"""Entity ID"""
    entity_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_type') }})
    r"""Entity type"""
    files: List[Files] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files') }})
    
