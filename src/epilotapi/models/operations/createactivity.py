import dataclasses
from typing import Optional
from ..shared import activity as shared_activity
from ..shared import activityitem as shared_activityitem


@dataclasses.dataclass
class CreateActivityQueryParams:
    entities: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entities', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class CreateActivityRequest:
    query_params: CreateActivityQueryParams = dataclasses.field()
    request: Optional[shared_activity.Activity] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateActivityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    activity_item: Optional[shared_activityitem.ActivityItem] = dataclasses.field(default=None)
    
