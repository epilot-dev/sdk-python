import dataclasses
from typing import Optional
from ..shared import activityitem as shared_activityitem
from ..operations import activityitem as operations_activityitem


@dataclasses.dataclass
class GetActivityPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetActivityQueryParams:
    operations_from: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'operations_from', 'style': 'form', 'explode': True }})
    operations_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'operations_size', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetActivityRequest:
    path_params: GetActivityPathParams = dataclasses.field()
    query_params: GetActivityQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetActivityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    activity_item: Optional[shared_activityitem.ActivityItem] = dataclasses.field(default=None)
    
