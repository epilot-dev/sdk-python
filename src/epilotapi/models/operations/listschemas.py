from __future__ import annotations
import dataclasses
from ..shared import entityschemaitem as shared_entityschemaitem
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Optional


@dataclasses.dataclass
class ListSchemasQueryParams:
    unpublished: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'unpublished', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListSchemasRequest:
    query_params: ListSchemasQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListSchemas200ApplicationJSON:
    results: Optional[list[shared_entityschemaitem.EntitySchemaItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListSchemasResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_schemas_200_application_json_object: Optional[ListSchemas200ApplicationJSON] = dataclasses.field(default=None)
    