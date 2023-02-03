import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import activityitem as shared_activityitem


@dataclasses.dataclass
class GetEntityActivityFeedPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetEntityActivityFeedQueryParams:
    after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    before: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    from_: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from', 'style': 'form', 'explode': True }})
    size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'size', 'style': 'form', 'explode': True }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': True }})
    

@dataclass_json
@dataclasses.dataclass
class GetEntityActivityFeed200ApplicationJSON:
    results: Optional[list[shared_activityitem.ActivityItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    total: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    

@dataclasses.dataclass
class GetEntityActivityFeedRequest:
    path_params: GetEntityActivityFeedPathParams = dataclasses.field()
    query_params: GetEntityActivityFeedQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetEntityActivityFeedResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_entity_activity_feed_200_application_json_object: Optional[GetEntityActivityFeed200ApplicationJSON] = dataclasses.field(default=None)
    
