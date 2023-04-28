"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityschemaitem as shared_entityschemaitem
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclasses.dataclass
class ListSchemasRequest:
    
    unpublished: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'unpublished', 'style': 'form', 'explode': True }})

    r"""Return unpublished draft schemas"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListSchemas200ApplicationJSON:
    r"""Success"""
    
    results: Optional[list[shared_entityschemaitem.EntitySchemaItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})

    

@dataclasses.dataclass
class ListSchemasResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    list_schemas_200_application_json_object: Optional[ListSchemas200ApplicationJSON] = dataclasses.field(default=None)

    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    