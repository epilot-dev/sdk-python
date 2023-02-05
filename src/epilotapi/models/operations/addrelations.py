import dataclasses
from ..shared import relationitem as shared_relationitem
from typing import Optional


@dataclasses.dataclass
class AddRelationsPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AddRelationsQueryParams:
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class AddRelationsRequest:
    path_params: AddRelationsPathParams = dataclasses.field()
    query_params: AddRelationsQueryParams = dataclasses.field()
    request: Optional[list[shared_relationitem.RelationItem]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AddRelationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    relation_item: Optional[shared_relationitem.RelationItem] = dataclasses.field(default=None)
    