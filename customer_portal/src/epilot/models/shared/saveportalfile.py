"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import origin_enum as shared_origin_enum
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavePortalFileFilesS3ref:
    
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})  
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavePortalFileFiles:
    
    file_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_type') }})  
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})  
    filename: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filename'), 'exclude': lambda f: f is None }})  
    s3ref: Optional[SavePortalFileFilesS3ref] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3ref'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavePortalFile:
    r"""Save portal file"""
    
    files: list[SavePortalFileFiles] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files') }})  
    origin: shared_origin_enum.OriginEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origin') }})
    r"""Origin of the portal"""  
    