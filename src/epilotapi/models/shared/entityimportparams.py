from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityImportParamsS3Reference:
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('bucket') }})
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityImportParams:
    s3_reference: EntityImportParamsS3Reference = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('S3Reference') }})
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema') }})
    