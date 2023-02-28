from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class DeleteRelationPathParams:
    attribute: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attribute', 'style': 'simple', 'explode': False }})
    entity_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entity_id', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteRelationQueryParams:
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class DeleteRelationRequest:
    path_params: DeleteRelationPathParams = dataclasses.field()
    query_params: DeleteRelationQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteRelationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    