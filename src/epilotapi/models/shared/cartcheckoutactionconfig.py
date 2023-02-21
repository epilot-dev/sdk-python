import dataclasses
from ..shared import cartcheckoutconfig as shared_cartcheckoutconfig
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class CartCheckoutActionConfig:
    r"""CartCheckoutActionConfig
    Creates an order entity with prices from journey
    """
    
    allow_failure: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('allow_failure') }})
    config: Optional[shared_cartcheckoutconfig.CartCheckoutConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('config') }})
    created_automatically: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_automatically') }})
    flow_action_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('flow_action_id') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    type: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    