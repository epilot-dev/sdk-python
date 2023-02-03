import dataclasses



@dataclasses.dataclass
class DeleteSchemaByIDPathParams:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteSchemaByIDQueryParams:
    id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class DeleteSchemaByIDRequest:
    path_params: DeleteSchemaByIDPathParams = dataclasses.field()
    query_params: DeleteSchemaByIDQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteSchemaByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    
