from __future__ import annotations
import dataclasses
from ..shared import taxonomyclassification as shared_taxonomyclassification
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClassificationsUpdate:
    create: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('create'), 'exclude': lambda f: f is None }})
    delete: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('delete'), 'exclude': lambda f: f is None }})
    update: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('update'), 'exclude': lambda f: f is None }})
    