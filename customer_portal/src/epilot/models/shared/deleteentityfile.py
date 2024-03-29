"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteEntityFile:
    r"""Delete file"""
    
    entity_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id') }})  
    entity_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_type') }})  
    file_entity_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_entity_ids') }})  
    