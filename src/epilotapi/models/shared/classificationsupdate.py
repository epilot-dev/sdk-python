import dataclasses
from ..shared import taxonomyclassification as shared_taxonomyclassification
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class ClassificationsUpdate:
    create: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('create') }})
    delete: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('delete') }})
    update: Optional[list[shared_taxonomyclassification.TaxonomyClassification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('update') }})
    