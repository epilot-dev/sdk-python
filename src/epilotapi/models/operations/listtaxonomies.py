import dataclasses
from ..shared import taxonomy as shared_taxonomy
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class ListTaxonomies200ApplicationJSON:
    results: Optional[list[shared_taxonomy.Taxonomy]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class ListTaxonomiesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_taxonomies_200_application_json_object: Optional[ListTaxonomies200ApplicationJSON] = dataclasses.field(default=None)
    