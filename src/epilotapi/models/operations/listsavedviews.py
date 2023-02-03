import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import savedviewitem as shared_savedviewitem


@dataclass_json
@dataclasses.dataclass
class ListSavedViews200ApplicationJSON:
    results: Optional[list[shared_savedviewitem.SavedViewItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class ListSavedViewsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_saved_views_200_application_json_object: Optional[ListSavedViews200ApplicationJSON] = dataclasses.field(default=None)
    
