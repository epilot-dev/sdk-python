import dataclasses
from typing import Optional
from ..shared import entityschema as shared_entityschema
from ..shared import entityschemaitem as shared_entityschemaitem


@dataclasses.dataclass
class CreateNewSchemaVersionPathParams:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateNewSchemaVersionQueryParams:
    draft: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'draft', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CreateNewSchemaVersionRequest:
    path_params: CreateNewSchemaVersionPathParams = dataclasses.field()
    query_params: CreateNewSchemaVersionQueryParams = dataclasses.field()
    request: Optional[shared_entityschema.EntitySchema] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateNewSchemaVersionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_schema_item: Optional[shared_entityschemaitem.EntitySchemaItem] = dataclasses.field(default=None)
    
