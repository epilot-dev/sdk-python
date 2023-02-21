import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class GetJourneyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetJourneyQueryParams:
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orgId', 'style': 'form', 'explode': True }})
    source: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'source', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetJourneyRequest:
    path_params: GetJourneyPathParams = dataclasses.field()
    query_params: GetJourneyQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetJourneyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    journey_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    