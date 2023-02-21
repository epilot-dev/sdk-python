import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class PatchUpdateJourneyRequest:
    request: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PatchUpdateJourneyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    journey_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    