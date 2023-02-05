import dataclasses
from ..shared import relationitem as shared_relationitem
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Optional


@dataclasses.dataclass
class UpdateRelationPathParams:
    attribute: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attribute', 'style': 'simple', 'explode': False }})
    entity_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'entity_id', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateRelationQueryParams:
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateRelationRequestBody:
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_tags') }})
    

@dataclasses.dataclass
class UpdateRelationRequest:
    path_params: UpdateRelationPathParams = dataclasses.field()
    query_params: UpdateRelationQueryParams = dataclasses.field()
    request: Optional[UpdateRelationRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateRelationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    relation_item: Optional[shared_relationitem.RelationItem] = dataclasses.field(default=None)
    