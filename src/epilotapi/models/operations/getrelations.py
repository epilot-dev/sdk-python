import dataclasses
from typing import Any,Optional


@dataclasses.dataclass
class GetRelationsPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetRelationsQueryParams:
    hydrate: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'hydrate', 'style': 'form', 'explode': True }})
    include_reverse: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include_reverse', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetRelationsRequest:
    path_params: GetRelationsPathParams = dataclasses.field()
    query_params: GetRelationsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetRelationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_relations_resp: Optional[list[Any]] = dataclasses.field(default=None)
    
