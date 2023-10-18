"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityImportParamsS3Reference:
    r"""The S3 bucket and key where the JSON file for import is located."""
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    r"""The name of the S3 bucket where the JSON file for import is stored."""
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""The key or path to the JSON file within the S3 bucket."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityImportParams:
    r"""The parameters for importing entities."""
    s3_reference: EntityImportParamsS3Reference = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('S3Reference') }})
    r"""The S3 bucket and key where the JSON file for import is located."""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    r"""The schema of the entities being imported. This must match the schema of the entities on the platform."""
    

