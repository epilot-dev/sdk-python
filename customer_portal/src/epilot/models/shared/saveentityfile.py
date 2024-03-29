"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from epilot import utils
from typing import Optional

class SaveEntityFileFilesAccessControlEnum(str, Enum):
    PRIVATE = "private"
    PUBLIC_READ = "public-read"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SaveEntityFileFilesS3ref:
    
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})  
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SaveEntityFileFiles:
    
    filename: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename') }})  
    s3ref: SaveEntityFileFilesS3ref = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref') }})  
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})  
    access_control: Optional[SaveEntityFileFilesAccessControlEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_control'), 'exclude': lambda f: f is None }})  
    document_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_type'), 'exclude': lambda f: f is None }})  
    file_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_entity_id'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SaveEntityFile:
    r"""Save file"""
    
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id') }})  
    entity_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_type') }})  
    files: list[SaveEntityFileFiles] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files') }})  
    