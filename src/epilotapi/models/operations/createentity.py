import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class CreateEntityPathParams:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateEntityQueryParams:
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'activity_id', 'style': 'form', 'explode': True }})
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CreateEntityRequest:
    path_params: CreateEntityPathParams = dataclasses.field()
    query_params: CreateEntityQueryParams = dataclasses.field()
    request: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_item: Optional[dict[str, Any]] = dataclasses.field(default=None)
    