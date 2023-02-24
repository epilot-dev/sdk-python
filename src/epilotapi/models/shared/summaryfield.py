from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SummaryField:
    r"""SummaryField
    Summary Fields are displayed inside list view as a resume of the relation entity.
    """
    
    display_as: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_as'), 'exclude': lambda f: f is None }})
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('field'), 'exclude': lambda f: f is None }})
    