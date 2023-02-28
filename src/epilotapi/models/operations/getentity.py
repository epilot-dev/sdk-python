from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetEntityPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetEntityQueryParams:
    hydrate: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'hydrate', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetEntityRequest:
    path_params: GetEntityPathParams = dataclasses.field()
    query_params: GetEntityQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetEntity200ApplicationJSON:
    entity: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity'), 'exclude': lambda f: f is None }})
    relations: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relations'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_entity_200_application_json_object: Optional[GetEntity200ApplicationJSON] = dataclasses.field(default=None)
    