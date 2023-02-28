from __future__ import annotations
import dataclasses
from ..shared import activityitem as shared_activityitem
from typing import Optional


@dataclasses.dataclass
class AttachActivityPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AttachActivityQueryParams:
    entities: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'entities', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class AttachActivityRequest:
    path_params: AttachActivityPathParams = dataclasses.field()
    query_params: AttachActivityQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class AttachActivityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    activity_item: Optional[shared_activityitem.ActivityItem] = dataclasses.field(default=None)
    