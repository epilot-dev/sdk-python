from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavedViewCreatedBy1:
    r"""SavedViewCreatedBy1
    A user that created the view
    """
    
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user_id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavedView:
    r"""SavedView
    A saved entity view
    """
    
    created_by: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    slug: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    ui_config: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('ui_config') }})
    org: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('org'), 'exclude': lambda f: f is None }})
    shared: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('shared'), 'exclude': lambda f: f is None }})
    