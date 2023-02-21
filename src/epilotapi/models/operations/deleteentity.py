import dataclasses
from typing import Optional


@dataclasses.dataclass
class DeleteEntityPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteEntityQueryParams:
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'activity_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class DeleteEntityRequest:
    path_params: DeleteEntityPathParams = dataclasses.field()
    query_params: DeleteEntityQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    