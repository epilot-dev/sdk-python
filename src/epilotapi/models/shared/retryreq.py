import dataclasses
from ..shared import retrystrategy_enum as shared_retrystrategy_enum
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class RetryReq:
    retry_strategy: Optional[shared_retrystrategy_enum.RetryStrategyEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('retry_strategy') }})
    