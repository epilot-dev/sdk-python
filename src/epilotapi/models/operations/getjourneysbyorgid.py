import dataclasses
from typing import Any,Optional


@dataclasses.dataclass
class GetJourneysByOrgIDPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetJourneysByOrgIDRequest:
    path_params: GetJourneysByOrgIDPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetJourneysByOrgIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_journeys_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    
