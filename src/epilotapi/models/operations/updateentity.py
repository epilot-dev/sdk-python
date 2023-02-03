import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional


@dataclasses.dataclass
class UpdateEntityPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateEntityQueryParams:
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'activity_id', 'style': 'form', 'explode': True }})
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class UpdateEntityRequest:
    path_params: UpdateEntityPathParams = dataclasses.field()
    query_params: UpdateEntityQueryParams = dataclasses.field()
    request: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_item: Optional[dict[str, Any]] = dataclasses.field(default=None)
    
