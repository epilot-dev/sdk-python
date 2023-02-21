import dataclasses
from dataclasses_json import dataclass_json
from epilotapi import utils
from typing import Any, Optional


@dataclasses.dataclass
class UpsertEntityPathParams:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpsertEntityQueryParams:
    activity_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'activity_id', 'style': 'form', 'explode': True }})
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'async', 'style': 'form', 'explode': True }})
    dry_run: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'dry_run', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclasses.dataclass
class UpsertEntityRequestBody:
    entity: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity') }})
    unique_key: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('unique_key') }})
    

@dataclasses.dataclass
class UpsertEntityRequest:
    path_params: UpsertEntityPathParams = dataclasses.field()
    query_params: UpsertEntityQueryParams = dataclasses.field()
    request: Optional[UpsertEntityRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpsertEntityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_item: Optional[dict[str, Any]] = dataclasses.field(default=None)
    