"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkflowContext:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    

