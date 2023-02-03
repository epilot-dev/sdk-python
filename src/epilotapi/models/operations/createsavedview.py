import dataclasses
from typing import Optional
from ..shared import savedview as shared_savedview
from ..shared import savedviewitem as shared_savedviewitem


@dataclasses.dataclass
class CreateSavedViewRequest:
    request: Optional[shared_savedview.SavedView] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateSavedViewResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    saved_view_item: Optional[shared_savedviewitem.SavedViewItem] = dataclasses.field(default=None)
    
