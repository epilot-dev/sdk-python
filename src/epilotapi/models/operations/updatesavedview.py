from __future__ import annotations
import dataclasses
from ..shared import savedview as shared_savedview
from ..shared import savedviewitem as shared_savedviewitem
from typing import Optional


@dataclasses.dataclass
class UpdateSavedViewPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateSavedViewRequest:
    path_params: UpdateSavedViewPathParams = dataclasses.field()
    request: Optional[shared_savedview.SavedView] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateSavedViewResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    saved_view_item: Optional[shared_savedviewitem.SavedViewItem] = dataclasses.field(default=None)
    