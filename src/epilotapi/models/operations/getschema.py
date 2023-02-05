import dataclasses
from ..shared import entityschemaitem as shared_entityschemaitem
from typing import Optional


@dataclasses.dataclass
class GetSchemaPathParams:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSchemaQueryParams:
    id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetSchemaRequest:
    path_params: GetSchemaPathParams = dataclasses.field()
    query_params: GetSchemaQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSchemaResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_schema_item: Optional[shared_entityschemaitem.EntitySchemaItem] = dataclasses.field(default=None)
    