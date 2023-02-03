import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import entityschemaitem as shared_entityschemaitem


@dataclasses.dataclass
class ListSchemasQueryParams:
    unpublished: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'unpublished', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclasses.dataclass
class ListSchemas200ApplicationJSON:
    results: Optional[list[shared_entityschemaitem.EntitySchemaItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class ListSchemasRequest:
    query_params: ListSchemasQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListSchemasResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_schemas_200_application_json_object: Optional[ListSchemas200ApplicationJSON] = dataclasses.field(default=None)
    
