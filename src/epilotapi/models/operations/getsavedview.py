import dataclasses
from ..shared import savedviewitem as shared_savedviewitem
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Optional


@dataclasses.dataclass
class GetSavedViewPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSavedViewRequest:
    path_params: GetSavedViewPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetSavedView200ApplicationJSON:
    view: Optional[shared_savedviewitem.SavedViewItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('view') }})
    

@dataclasses.dataclass
class GetSavedViewResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_saved_view_200_application_json_object: Optional[GetSavedView200ApplicationJSON] = dataclasses.field(default=None)
    