from __future__ import annotations
import dataclasses
from ..shared import errorcode_enum as shared_errorcode_enum
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ErrorOutput:
    error_code: shared_errorcode_enum.ErrorCodeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_code') }})
    error_reason: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('error_reason') }})
    